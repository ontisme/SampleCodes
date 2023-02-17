# requirements.txt
dnspython==2.2.1
filelock==3.8.0
idna==3.3

pip install git+https://gitea.ksol.io/karolyi/py3-validate-email@v1.0.9

import threading
from ipaddress import IPv4Address, IPv6Address
from validate_email import validate_email


lists = ["iqXOnxIWsM@gmail.com", "lLRVCIiLVZ@gmail.com", "DNeRuwtQrH@gmail.com", "DtsMCLkFoK@gmail.com"]

lists2 = ["2ad991q6a0@lelsm.ink", "ate4wxqsen@lelsm.ink", "x87e4xv7s8@kongkong66.top", "c28fynh5hp@hkwx.vip"]

def check_email_valid(email: str):
    is_valid = validate_email(
        email_address=email,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        smtp_helo_host='my.host.name',
        smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False,
        address_types=frozenset([IPv4Address, IPv6Address]))

    print(f"{email}: {is_valid}")


for i in lists:
    threading.Thread(target=check_email_valid, args=(i,)).start()

for i in lists2:
    threading.Thread(target=check_email_valid, args=(i,)).start()

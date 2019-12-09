import requests as r
import time
from encrypt.encrypt_md5 import encryption_md5 as m5
import execjs


def get_encrypt(pwd, ):
    with open('./js_migy_video.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    result = ctx.call('get_pwd', pwd)
    return result.split('*#*#*')


def login(username, pwd):
    url = 'https://passport.migu.cn/authn'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    enpwd, fingerPrint, fingerPrintDetail = get_encrypt(pwd)
    data = {
        'loginID': username,
        'enpassword': enpwd,
        'fingerPrint': fingerPrint,
        'fingerPrintDetail': fingerPrintDetail,
        'isAsync': 'true',
        'imgcodeType': '1',
        'appType': '2',
        'sourceID': '203021',
        'relayState': 'login',

    }
    html = r.post(url=url, headers=headers, data=data)
    print(html)
    print(html.text)


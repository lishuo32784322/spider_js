# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree

r = r.Session()

def get_pic():
    s = list(str(time.time()).replace('.', ''))
    s.insert(-4, '.')
    url = 'https://passport.tuniu.com/ajax/captcha/v/{}'.format(''.join(s))
    headers = {'referer': 'https://passport.tuniu.com/login?origin=https://www.tuniu.com/ssoConnect', 'sec-fetch-mode': 'no-cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    pic = r.get(url, headers=headers)
    with open('./code.jpg', 'wb') as f:
        f.write(pic.content)

def get_pwd(password):
    with open('./js_login_tuniu.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('hex_md5', password)
    return pwd

def login(username, password):
    get_pic()
    pwd = get_pwd(password)
    url = 'https://passport.tuniu.com/login/post'
    headers = {''
               'origin': 'https://passport.tuniu.com',
               'referer': 'https://passport.tuniu.com/login?origin=https://www.tuniu.com/ssoConnect',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
               }
    data = {'isWeak': '0',
            'login_type': 'P-N',
            'intlCode': ' ', 
            'username': username,
            'password': pwd,
            'identify_code': input('code:')
            }
    html = r.post(url=url, headers=headers, data=data)
    print(html)
    print(html.cookies)

login('17612472355', 'lishuo4322')

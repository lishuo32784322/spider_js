# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree

def get_pwd(dc, password):
    with open('./js_kongzhongwang_login.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('encrypt', dc, password)
    return pwd


def get_dc(r1):
    _time = str(time.time()).replace('.', '')[:-4]
    url = 'https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_={}'.format(_time)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Referer': 'https://passport.kongzhong.com/login',
        'Sec-Fetch-Mode': 'no-cors',
    }
    params = {
        'j': 'j',
        'jsonp': 'j',
        'service': 'https://passport.kongzhong.com/',
        '_': _time,
    }
    html = r1.get(url=url, headers=headers, params=params)
    return ''.join(re.findall('"dc":"(.*?)"', html.text))

def login(username, password):
    r1 = r.Session()
    dc = get_dc(r1)
    pwd = get_pwd(dc, password)
    _time = str(time.time()).replace('.', '')[:-4]
    with open('./code.jpg', 'wb') as f:
        f.write(r.get('https://sso.kongzhong.com/createVCode?w=80&h=30&0.03372378348012428').content)
    code = input('code:')
    url = 'https://sso.kongzhong.com/ajaxLogin?j=j&&type=1&service=https://passport.kongzhong.com/&username={}&password={}&vcode={}&toSave=0&_={}'.format(username, pwd, code, _time)
    headers = {
        'Referer': 'https://passport.kongzhong.com/login',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    params = {
        'j': 'j',
        '': '',
        'type': '1',
        'service': 'https: // passport.kongzhong.com /',
        'username': username,
        'password': pwd,
        'vcode': code,
        'toSave': '0',
        '_': _time,
    }
    print(params)
    html = r.get(url=url, headers=headers, params=params)
    print(html)
    print(html.text)

login('17612472355', 'lishuo4322')
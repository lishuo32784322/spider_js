# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree


def get_pwd(pwd):
    with open('./login_fangjiawang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', pwd)
    return pwd

def get_code_token():
    with open('./login_fangjiawang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('guid')
    return pwd

def get_time():
    with open('./login_fangjiawang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('my_time')
    return pwd

def login(username, password):
    rs = r.Session()
    codeToken = get_code_token()
    _pass = get_pwd(password)
    def get_code(rs):
        _time = get_time()
        url = 'https://www.fangjia.com/randomCode'
        params = {
            'codeToeken': codeToken,
            'time': str(_time)+'"'
        }
        code = rs.get(url=url, params=params)
        with open('./code.jpg', 'wb') as f:
            f.write(code.content)

    get_code(rs)
    url = 'https://www.fangjia.com/user/userLogin'
    headers = {
        'Host': 'www.fangjia.com',
        'Origin': 'https://www.fangjia.com',
        'Referer': 'https://www.fangjia.com/user/login',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    data = {
        'username': username,
        'code': input('code:'),
        'pass': _pass,
        'codeToken': codeToken,
    }
    html = rs.post(url=url, headers=headers, data=data)
    print(html)
    print(html.text)


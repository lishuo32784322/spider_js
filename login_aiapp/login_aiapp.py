# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree


def get_pwd(password):
    with open('./login_aiapp.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', password)
    return pwd

def login(username, password):
    url = 'http://www.iappstoday.com/ajax/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Referer': 'http://www.iappstoday.com/',
    }
    pwd = get_pwd(password)
    data = {
        'username': username,
        'password': pwd,
    }
    html = r.post(url=url, headers=headers, data=data)
    print(html)
    print(html.text)

login('17612472355', 'lishuo4322')
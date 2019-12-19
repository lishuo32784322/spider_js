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
    with open('./login_soufangbang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', password)
    return pwd


def login(username, password):
    pwd = get_pwd(password)
    url = 'https://passport.fang.com/login.api'
    headers = {
        'Referer': 'http://2.fang.com/Default.aspx',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    params = {'callback': 'myCallBack',
              'Uid': username,
              'Pwd': pwd,
              'Service': 'esf-agent-web',
              'IP': '',
              'VCode': 'undefined',
              'AutoLogin': '0',
              '_': str(int(time.time()*1000))
    }
    html = r.get(url=url, headers=headers, json=params)
    print(html)
    print(html.text)

login('17612472355', 'lishuo4322')
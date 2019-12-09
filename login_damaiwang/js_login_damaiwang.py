# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree


def get_sign(pwd):
    with open('./js_login_damaiwang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', pwd)
    return pwd


def get_pwd(username, password):
    pwd = get_sign(password)
    url = 'https://ipassport.damai.cn/newlogin/login.do?appName=damai&fromSite=-2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    data = {
        'keepLogin': 'false',
        'umidGetStatusVal': '255',
        'screenPixel': '1920x1080',
        'navlanguage': 'zh-CN',
        'navUserAgent': headers['User-Agent'],
        'navPlatform': 'Linux x86_64',
        'appEntrance': 'damai',
        'appName': 'damai',
        'fromSite': '-2',
        'isMobile': 'false',
        'lang': 'zh_CN',
        'mobile': 'false',
        'returnUrl': 'https://passport.damai.cn/dologin.htm?redirectUrl=https%3A%2F%2Fwww.damai.cn&platform=106002',

        'loginId': username,
        'password2': pwd,
        'ua': '',
        'csrf_token': '',
        'umidToken': '',
    }
    html = r.post(url=url, headers=headers, data=data)
    print(html)
    print(html.text)


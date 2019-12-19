# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
from urllib.parse import urlencode
import execjs
import hashlib
import requests as r
from lxml import etree


def get_pwd(password):
    with open('./login_caixinwang.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', password)
    return pwd

def login(username, password):
    pwd = get_pwd(password)
    url = 'https://gateway.caixin.com/api/ucenter/user/v1/loginJsonp?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    params = {
        'callback': 'jQuery17206654402952322176_1576739873055',
        'account': username,
        'password': pwd,
        'device': 'CaixinWebsite',
        'deviceType': '5',
        'unit': '1',
        'userTag': 'null',
        'areaCode': '+86',
        '_': str(int(time.time() * 1000))
    }
    url = url + urlencode(params)
    print(url)
    html = r.get(url=url, headers=headers, json=params)
    print(html)
    print(html.text)


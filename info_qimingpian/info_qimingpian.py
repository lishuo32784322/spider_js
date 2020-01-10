# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree


def decode_info(s):
    with open('./js_info_qimingpian.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_info', s)
    return pwd

def get_info():
    url = 'https://vipapi.qimingpian.com/DataList/productListVip'
    headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.qimingpian.cn', 'Sec-Fetch-Mode': 'cors', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    data = {'time_interval': '', 'tag': '', 'tag_type': '', 'province': '', 'lunci': '', 'page': '1', 'num': '20', 'unionid': ''}
    html = r.post(url=url, headers=headers, data=data)
    print(decode_info(html.json().get('encrypt_data')).get('list'))

get_info()
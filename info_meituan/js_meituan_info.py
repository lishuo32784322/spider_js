# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import zlib
import json
import random
import base64
import execjs
import hashlib
import requests as r
from lxml import etree
import urllib.parse


def get_token(areaId, cateId, page, cityName, originUrl):
    uuid = ''.join([random.choice('0123456789abcdef') for _ in range(20)]) + '.' + str(int(time.time())) + '.1.0.0'
    sign = base64.b64encode(zlib.compress(
                    (
                       f"areaId={areaId}&cateId={cateId}&cityName={cityName}&dinnerCountAttrId=&"
                       f"optimusCode=10&originUrl={originUrl}&page={page}&partner=126&platform=1&"
                       f"riskLevel=1&sort=&userId=&uuid={uuid}"
                    ).encode()
                )
            ).decode()
    ts = int(time.time() * 1000)
    token = {
        "rId":100900,
        "ver":"1.0.6",
        "ts":ts,
        "cts":ts + random.randint(100, 150),
        "brVD":[1853, 921],
        "brR":[[1920, 1080], [1853, 1053], 24, 24],
        "bI":[originUrl, ""],
        "mT":[],
        "kT":[],
        "aT":[],
        "tT":[],
        "aM":"",
        "sign": sign
    }
    _token = base64.b64encode(zlib.compress(str(token).encode())).decode()
    return _token


def get_info():
    url = 'https://bj.meituan.com/meishi/api/poi/getPoiList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Referer': 'https://bj.meituan.com/meishi/c393/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
    }
    params = {'cityName': '北京', 'cateId': '393', 'areaId': '0', 'sort': '', 'dinnerCountAttrId': '', 'page': '1', 'userId': '', 'uuid': 'f934dd4d35fd48a0a73f.1576134771.1.0.0', 'platform': '1', 'partner': '126', 'originUrl': 'https://bj.meituan.com/meishi/c393/', 'riskLevel': '1', 'optimusCode': '10'}
    token_json = params
    token_json['_token'] = get_token(params['areaId'], params['cateId'], params['page'], params['cityName'], params['originUrl'])

    html = r.get(url=url, headers=headers, json=token_json)
    print(html)
    print(html.text)


get_info()
uuid = ''.join([random.choice('0123456789abcdef') for _ in range(20)]) + '.' + str(int(time.time())) + '.1.0.0'
print(uuid)
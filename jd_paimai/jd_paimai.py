# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import random
import binascii
import hashlib
import requests as r
from lxml import etree


def baseN(num, b):
    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


def get_info():
    url = 'https://api.m.jd.com/api'
    headers = {
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    print(random.random())
    s = int(random.random() * 2147483648)
    print(s)
    s = baseN(s, 36)
    print(s)
    jsonp = 'jQuery{}'.format(s)
    data = {'appid': 'paimai-search-soa', 'functionId': 'paimai_unifiedSearch', 'body': '{"apiType":2,"reqSource":1,"childrenCateId":"12728","paimaiStatus":"","displayStatus":"","sortField":8,"keyword":"","paimaiTimes":"","provinceId":"1","cityId":"","countyId":"","loan":"","purchaseRestriction":"","currentPriceRangeStart":"","currentPriceRangeEnd":"","pageSize":40,"page":7}', 'loginType': '2', 'jsonp': 'jQuery310024571114585128817_1576571684760', '_': '1576571684762'}
    # print(data)
    html = r.get(url=url, headers=headers, json=data)
    print(html)
    print(html.text)

get_info()

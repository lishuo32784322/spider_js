# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree


def get_info():
    url = 'https://flights.ctrip.com/itinerary/api/12808/products'
    headers = {
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'origin': 'https://flights.ctrip.com',
        'content-type': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'accept': '*/*'
    }
    data = {
        "flightWay":"Oneway",
        "classType":"ALL",
        "hasChild":'false',
        "hasBaby":'false',
        "searchIndex":'1',
        "date":"2020-01-17",
        "airportParams":[{"dcity":"BJS","acity":"CAN","dcityname":"北京","acityname":"广州","date":"2020-01-17","dcityid":1,"acityid":32}],
        # "token":"be030ce3f1f7cce352e6077543dcaa25"
            }
    html = r.post(url=url, headers=headers, json=data)
    print(html)
    print(html.text)

get_info()
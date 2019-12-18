# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import hashlib
import requests as r
from lxml import etree


def get_info():
    url = 'https://meishi.meituan.com/i/api/channel/deal/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'x-requested-with': 'XMLHttpRequest',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'https://meishi.meituan.com',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://meishi.meituan.com/i/?ci=60&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
    }
    data = {"uuid":"f934dd4d35fd48a0a73f.1576134771.1.0.0","version":"8.2.0","platform":3,"app":"","partner":126,"riskLevel":1,"optimusCode":10,"originUrl":"http://meishi.meituan.com/i/?ci=60&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1","offset":0,"limit":15,"cateId":1,"lineId":0,"stationId":0,"areaId":0,"sort":"default","deal_attr_23":"","deal_attr_24":"","deal_attr_25":"","poi_attr_20043":"","poi_attr_20033":""}
    html = r.post(url=url, headers=headers, json=data)
    print(html)
    print(html.text)


get_info()
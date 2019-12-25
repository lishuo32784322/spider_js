# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import urllib
import hashlib
import requests as r
from lxml import etree


class Cods:
    validate_api = "http://120.78.10.176:3000/api/geetest/v3?"  # 外网接口
    challenge_url = 'https://ss.cods.org.cn/gc/geetest/query?t={}'
    search_list_url = 'https://ss.cods.org.cn/latest/searchR?{}'

    fetch = r.session()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'ss.cods.org.cn',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    def __init__(self, q):
        self.q = q

    def get_list_page(self):
        challenge = self.fetch.get(url=self.challenge_url.format(int(time.time())), headers=self.headers)
        print(0, challenge.text)
        result = eval(challenge.json())
        challenge = result['challenge']
        gt = result['gt']
        query = {
            'gt': gt,
            'challenge': challenge,
        }
        url = self.validate_api + urllib.parse.urlencode(query)
        validate = self.fetch.get(url=url)
        print(1, validate.text)
        validate_data = validate.json().get('validate', ' ')
        query_params = {
            'q': self.q,
            't': 'common',
            'currentPage': '1',
            'searchToken': '',
            "geetest_challenge": query['challenge'],
            "geetest_validate": validate_data,
            "geetest_seccode": validate_data + "|jordan"
        }
        search_list = self.fetch.get(url=self.search_list_url.format(urllib.parse.urlencode(query_params)))
        print(2, search_list.text)

if __name__ == '__main__':
    c = Cods('探迹')
    c.get_list_page()
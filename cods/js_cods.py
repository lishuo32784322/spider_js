# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import hashlib
import requests as r
from lxml import etree


def get_list_page():
    url = 'https://ss.cods.org.cn/latest/searchR?q=%25E6%258E%25A2%25E8%25BF%25B9&t=common&currentPage=1&searchToken=&geetest_challenge=eadd421600239d97b4f4010911a298e5eu&geetest_validate=2272e5eb6236fdc495e76193779d9b02&geetest_seccode=2272e5eb6236fdc495e76193779d9b02|jordan'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    cookies = {
        'Cookie': 'kefuCookie=508c19ad9ae645c497a697e4c6c68623; __utma=48894260.1565065399.1575604040.1575604040.1575604040.1; __utmc=48894260; __utmz=48894260.1575604040.1.1.utmcsr=im.dingtalk.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.3.1565065399.1575604040; _gid=GA1.3.1008186644.1575604040; JSESSIONID=F9EA5819CE60DEFCE48E04EE91F5FA36; userCookie=d05f225a-f1f4-4dfc-bfda-de94068fb1fc; key=%5B%7B%22title%22%3A%22%E6%8E%A2%E8%BF%B9%22%2C%20%22link%22%3A%22wx_searchPro.action%3Fkeyword%3D%E6%8E%A2%E8%BF%B9%22%2C%20%22other%22%3A%22%22%7D%5D; __utmt=1; __utmb=48894260.2.10.1575604040; Hm_lvt_f4e96f98fa73da7d450a46f37fffbf56=1575604040,1575604850; Hm_lpvt_f4e96f98fa73da7d450a46f37fffbf56=1575604850'
    }
    params = {
        'q': '%E6%8E%A2%E8%BF%B9',
        't': 'common',
        'currentPage': '1',
        'searchToken': '',
        'geetest_challenge': 'eadd421600239d97b4f4010911a298e5eu',
        'geetest_validate': '2272e5eb6236fdc495e76193779d9b02',
        'geetest_seccode': '2272e5eb6236fdc495e76193779d9b02|jordan'
    }
    html = r.get(url=url, headers=headers, params=params, cookies=cookies)
    print(html)
    print(html.text)

get_list_page()
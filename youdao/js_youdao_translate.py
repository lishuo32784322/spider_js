# -*- coding:utf-8 -*-
import time
import random
from encrypt.encrypt_md5 import encryption_md5 as m5
import requests


def youdao_translate(query):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://fanyi.youdao.com/',
        'Host': 'fanyi.youdao.com',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1903986337@114.244.1.247; _ntes_nnid=73551e28d3a3bd17abdd98b393abbb5b,1571802802846; OUTFOX_SEARCH_USER_ID_NCOO=939222228.1799573; _ga=GA1.2.517712630.1571802853; JSESSIONID=abcHWBDht33JT7tBYFk5w; P_INFO=m17612472355; ANTICSRF=cleared; NTES_OSESS=cleared; S_OINFO=; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1574143881090',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '264',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    salt = str(int(time.time() * 1000) + random.randint(0, 10))
    ts = salt[:-1]
    bv = m5(headers['User-Agent'].split('Mozilla/')[1])
    sign = m5("fanyideskweb{}{}n%A-rKaT5fb[Gy?;N5@Tj".format(query, salt))

    data = {
        'i': query,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    html = requests.post(url=url, headers=headers, data=data)
    print(html.json())

youdao_translate("我爱你")




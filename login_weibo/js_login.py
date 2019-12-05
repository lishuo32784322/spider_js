# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import requests as r
from lxml import etree


def get_sign(username, pwd, servertime, nonce):
    with open('./js_login.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    su = ctx.call('get_su', username)
    sp = ctx.call('get_sp', pwd, servertime)
    return su, sp

def weibo_login(username, password, servertime, nonce, rsakv, prelt):
    r_session = r.Session()
    url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    su, sp = get_sign(username, password, servertime, nonce)
    data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pagerefer': '',
        'vsnf': '1',
        'service': 'miniblog',
        'servertime': servertime,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': prelt,
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
        'nonce': 'XVS2WU',
        'su': su,
        'sp': sp,
    }
    html = r_session.post(url=url, headers=headers, data=data)
    login_redirect = html.content.decode("GBK")
    print(login_redirect)
    pa = r'location\.replace\([\'"](.*?)[\'"]\)'
    redirect_url = re.findall(pa, login_redirect)[0]
    print(redirect_url)
    result = r_session.get(url=redirect_url)
    result = result.content.decode('GBK')
    pa = r'location\.replace\([\'"](.*?)[\'"]\)'
    result_url = re.findall(pa, result)[0]
    result = r_session.get(url=result_url)
    print(result)
    print(result.text)

def get_data():
    url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.19)&_={}'.format(int(time.time()))
    headers = {
        'Referer': 'https://weibo.com/',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    html = r.get(url, headers=headers)
    html = json.loads(''.join(re.findall('{.*}', html.text)))
    weibo_login('17612472355', 'lishuo4322', html['servertime'], html['nonce'], html['rsakv'], html['exectime'])

get_data()

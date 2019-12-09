# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree

def get_pwd(password):
    with open('./js_taobao_login.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('encrypt', password)
    return pwd


def login(username, password):
    pwd = get_pwd(password)
    print(pwd)
    url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    data = {
        'TPL_password': '',
        'ncoSig': '',
        'ncoSessionid': '',
        'slideCodeShow': 'false',
        'useMobile': 'false',
        'lang': 'zh_CN',
        'loginsite': '0',
        'newlogin': '0',
        'TPL_redirect_url': 'https://www.taobao.com/',
        'from': 'tbTop',
        'fc': 'default',
        'style': 'default',
        'css_style': '',
        'keyLogin': 'false',
        'qrLogin': 'true',
        'newMini': 'false',
        'newMini2': 'false',
        'tid': '',
        'loginType': '3',
        'minititle': '',
        'minipara': '',
        'pstrong': '',
        'sign': '',
        'need_sign': '',
        'isIgnore': '',
        'full_redirect': '',
        'sub_jump': '',
        'popid': '',
        'callback': '',
        'guf': '',
        'not_duplite_str': '',
        'need_user_id': '',
        'poy': '',
        'gvfdcname': '10',
        'gvfdcre': '',
        'from_encoding': '',
        'sub': 'false',
        'loginASR': '1',
        'loginASRSuc': '1',
        'allp': '',
        'oslanguage': 'zh-CN',
        'sr': '1920*1080',
        'osVer': '',
        'naviVer': 'chrome|77.0386512',
        'osACN': 'Mozilla',
        'osAV': '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'osPF': 'Linux x86_64', 'miserHardInfo': '',
        'appkey': '00000000', 'nickLoginLink': '',
        'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9FtFgri&f=top&redirectURL=https://www.taobao.com/&useMobile=true',
        'showAssistantLink': 'false',
        'TPL_username': username,
        'TPL_password_2': pwd,
        'um_token': 'T201A93DDA84633B5E54134720068EE37391F282C44597FAF5C9D2FC1D5',
        'ncoToken': '3d2c57ab9d5e0558bb8e7a287df7ffa0a588e2f6',
        'ua': '121#9Uylk+ru9aQlVlwPxVmElVvYecEfKujVlGgiqqxImBv8O3hJFID5lwLYAcFfKujVllgm+aVokJXSA3rnE9jIlwXYLa+xNvo9lGuYZ7pIKM9STQrJEmD5lwLYAcfdK5jVVmgY+zP5KMlVA3rnEkD5bwLYOcMYHskEGQQVBIbvsbc9MtFPD0rOXaFbbZ3glWfopCibkZ0T83Smbgi0CeIAFtdEmkQvnjxSpqLbCZeTM35O3piDkeHXmo60bZienqC9pCibCZ0T83BhbZs0keHaF9FbbZsbnjxSpXsbMqAi8dBLbgi0CNHaC9BQb7/0wqqZp9sbC6748u/mNlqLhaGwt5c79bEZk2Dfk9Eg7fdNxF/SVFWaeNfAgRAEkBd3ostepzOpFg2B0CySqFkhwMf46o6F4n1fi20sbKFxI+10h9hodvU91a0lePxWGLAyTtwNFASchEXj1B6LzNlJsXA0EPEN2h+HOneRHbhUW1e83GpP3N0AHBWK+MhPrZWWE5S7sDCFrqLvGTb2OiTMn1rr3/lHvJ0F/WaVqo92j8656pbpMcUxQyrz/BGt3u+jG5xa6TY6Fg86ENlhKG7/rGFVzyxGeOw0DUMA6ioCk3xq90h3j19zeIJV2IzxUxxEjwvldb5o+4Rfct89voa0ULMQdSZsacYpCj2dkBgrz0jQxnGZ/csF59fcmx6AKm+gso/k3jqPrv9v+JZs88MQhAa3kfuBedrtuxP5tF8oNAV7sqsWg9Gi15W9IAl4YNaAmDQJXVBb4ybooYljRsR/tt3dDLhmExY5WM/F+AHXbhYsc3cwxeBefDZN8UJ+mTQOwzHI8Qw73IFs/QXdu1aNsy8vgojZ5xTJ7Mr+bjzBZHm9XaMBIGy0AEpC054RzHIISRp4tpHCOffasA7zf+SPRpR1PVxRn69qeIQOmC0xMUnuUMmS60ikSiGs47bQ6qWhJSOJbcXN4c0qP0hxUzP2ts61QOlk/v9jTSExg3OXgxIMN7md3oJfZZjo9BoGLztcR40DXuproMoH2wLII1F2lLBkMSpproVXzBYfMhTJuVDAawrmXdN1FAN5R4P3bxaCIFV0gSoDNDe8r8+/nMvb0b3Rr84jLx53WVXW9zI00sTZXfpLzovnUgYw0WgZlCmd6vpNQITSTpz8PAe59IR4JNnxFvYHoS8/YVaasukC9VsrtVbbNsD4Iteuf+KxaddDo+c+bl0BUYwX2jxyc6/WHXKyX04kWqACdEfnPvg6Rn9ZV8d2kGG4ugZ8Kzj8DhsnzDysWDPZE0LI6heOIkabfeiozO5On/GfobBNAsyDFsgp0qj6vWI7TqiXLUPjsfZuL/hKEO2bf75MRZHoU/0X/4Dk7EOm5c6sAJVz6JQVQqLD6O1zyeA0abr8RCIDmxlKaZt50fNG',
    }
    html = r.post(url=url, headers=headers, data=data)
    print(html)
    print(html.text)
    print(html.cookies)


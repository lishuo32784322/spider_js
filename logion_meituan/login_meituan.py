# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
from urllib.parse import urlencode
import execjs
import hashlib
import requests as r
from lxml import etree


def get_pwd(password):
    with open('./login_meituan.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    pwd = ctx.call('get_pwd', password)
    return pwd

def login(username, password):
    pwd = get_pwd(password)
    print(pwd)

login('123','lishuo')


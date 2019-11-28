import requests as r
import hashlib
import time
from encrypt.encrypt_md5 import encryption_md5 as m5


def get_sign(param):
	p = ''
	l = ["method", "orderTypeId", "orgcode", "pageNo", "pageSize", "plat", "platform", "shopId", "t", "v", "versionName"]
	for i in l:
		m = param[i]
		p += m
	r = '6C57AB91A1308E26B797F4CD382AC79D'
	f = param['method'] + p + r
	return m5(f).upper()

def f():
	t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	url = 'http://product.ddky.com/product/queryOrgcodeProductListForB2C.htm?'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
	}
	param = {
		'method': 'ddsy.product.query.orgcode.product.list.b2c',
		'orderTypeId': '0',
		'orgcode': '010101,010104',
		'otcMark': '1,2,99',
		'pageNo': '1',
		'pageSize': '100',
		'plat': 'H5',
		'platform': 'H5',
		'shopId': '-1',
		't': t,
		'v': '1.0',
		'versionName': '3.2.0',
	}
	param['sign'] = get_sign(param)
	html = r.get(url, headers=headers, params=param)
	print(html)
	print(html.text)

f()
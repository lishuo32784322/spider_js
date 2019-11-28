import requests as r
import time
from encrypt.encrypt_md5 import encryption_md5 as m5
import execjs


def f1(page):
	url = 'https://nyloner.cn/proxy'
	page = page
	num = 15
	t = int(time.time())
	token = m5('{}{}{}'.format(page, num, t))
	param = {
		'page': page,
		'num': num,
		't': t,
		'token': token,
	}
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
	}
	cookies = {
		'sessionid': 'yuq1gplqb4tfyhcgigp3nwewb052vrxy'
	}
	html = r.get(url=url.format(page, num, token, t), headers=headers, params=param, cookies=cookies)
	print(html.json())
	with open('./js_lingdu_ip.js', 'r', encoding='utf-8') as f:
		ctx = execjs.compile(f.read())
	return ctx.call('decode_str', html.json()['list'])


print(f1(1))


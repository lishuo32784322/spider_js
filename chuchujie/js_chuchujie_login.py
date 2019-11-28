import requests as r
from encrypt.encrypt_md5 import encryption_md5 as m5


def f(username, password):
	url = 'http://seller.chuchujie.com/sqe.php?s=/AccountSeller/login'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
	}
	data = {
		'username': username,
		'password': m5(password)
	}
	html = r.post(url=url, headers=headers, data=data)
	print(html)
	print(html.text)

f('17612472355', 'LI_shuo4322')
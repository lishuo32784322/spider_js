import requests as r


def f1(username, password):
	url = 'https://passport.58.com/58/login/pc/dologin'
	headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
		'origin': 'https://passport.58.com'
	}
	data = {
		'username': username,
		'password': '',
	}
	html = r.post(url=url, headers=headers, data=data)
	print(html)
	print(html.text)

f1('17612472355', 'lishuo4322')
import requests as r
import execjs


def get_sign(pwd):
    with open('./js_fenbi_login.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    sign = ctx.call('get_pwd', pwd)
    return sign

def f1(iphone, pwd):
	url = 'https://tiku.fenbi.com/api/users/loginV2?kav=12&app=web'
	data = {
		'password': get_sign(pwd),
		'persistent': 'true',
		'app': 'web',
		'phone': iphone,
	}
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
	}
	html = r.post(url, data=data, headers=headers)
	print(html)
	print(html.text)

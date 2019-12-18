# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import hashlib
import requests as r
from lxml import etree
from pymongo import MongoClient


mc = MongoClient()
def get_city():
    city_list = [i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM']
    for city in city_list:
        url = 'http://i.meituan.com/index/changecity/more/{}?cevent=imt%2FselectCity%2Fmore'.format(city)
        print(url)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Host': 'i.meituan.com',
        }
        cookies = {
            'Cookie': '__mta=152526086.1576482073923.1576483117967.1576483137741.9; __mta=152526086.1576482073923.1576482502542.1576483113165.7; uuid=f934dd4d35fd48a0a73f.1576134771.1.0.0; _lxsdk_cuid=16ef8f402ebc8-07b44a0b5be073-30720159-1fa400-16ef8f402ebc8; ci=1; rvct=1; JSESSIONID=1gobz0dpu0h4y1rlcy8clc0l2z; IJSESSIONID=1gobz0dpu0h4y1rlcy8clc0l2z; iuuid=8AF65F1DFCD36145322343D5D42BB17ABFE104CA4E484866B0F9747590F39D50; cityname=%E5%8C%97%E4%BA%AC; __utmc=74597006; _lxsdk=8AF65F1DFCD36145322343D5D42BB17ABFE104CA4E484866B0F9747590F39D50; mtcdn=K; _hc.v=017a6aee-28aa-6e54-3eb6-b5a12b51ca46.1576477534; lat=39.950256; lng=116.34784; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; ci3=1; __utma=74597006.1143626479.1576468806.1576468806.1576482074.2; __utmz=74597006.1576482074.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); idau=1; __mta=152526086.1576482073923.1576482273195.1576482358272.4; i_extend=H__a100002__b2; webloc_geo=39.91656%2C116.477224%2Cwgs84%2C-1; latlng=39.91656,116.477224,1576483114378; webp=1; __utmb=74597006.29.9.1576483117640; _lxsdk_s=16f0d434fb4-19c-9fb-dda%7C%7C158'
        }
        html = r.get(url=url, headers=headers, cookies=cookies)
        html = etree.HTML(html.text)
        lis = html.xpath('//div[@class="wrapper"]/ul//li')
        for li in lis:
            result = {}
            result['city_name'] = ''.join(li.xpath('./a/text()'))
            result['city_href'] = 'http:'+''.join(li.xpath('./a/@href'))
            result['city_gaevent'] = ''.join(li.xpath('./a/@gaevent'))
            result['city_data-citypinyin'] = ''.join(li.xpath('./a/@data-citypinyin'))
            mc.meituan.all_city.save({'_id': result['city_href'],'city_name': result['city_name'], 'city_href': result['city_href'], 'city_gaevent': result['city_gaevent'], 'city_data-citypinyin': result['city_data-citypinyin']})
            print(result)
# get_city()
for index, i in enumerate(mc.meituan.all_city.find()):
    print(index, i)
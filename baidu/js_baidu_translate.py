# -*- coding:utf-8 -*-
import requests
import execjs


def get_sign(query):
    with open('./js_baidu_translate.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    sign = ctx.call('e', query)
    return sign


def baidu_translate(query):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'cookie': 'BAIDUID=D8C62F30DC40C1BA85E5882510F31D8F:FG=1; PSTM=1571810415; BIDUPSID=B74D8392370FB89E8882E584ACA27A93; __cfduid=d7ae42fe661bb4419b2700cfecd11c7a21572338662; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=137151_137734_137867_136749_136757_137658_135846_128149_136436_137960_120165_137709_137381_137717_136381_137979_132909_136456_137690_131247_137749_132378_136681_118888_118869_118849_118821_118805_107318_136799_136431_136093_133352_137900_136862_138146_138115_129654_136194_124639_137105_133847_132551_137468_129644_131423_137742_137970_137466_136537_137722_110085_137863_127969_137912_138149_127417_136636_137207_137449_136988; BDUSS=9OWFJsc2VTdFJjZ3Vkcjh5bDJ2Z01QS2pQS09HVjJsWXNtVzEyWnFLRjkyZlZkRVFBQUFBJCQAAAAAAAAAAAEAAADdiEIzwO5TdXJl2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH1Mzl19TM5dUk; H_PS_PSSID=1459_21101_29568_29221_26350_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=-6KOJeCT5G3jcXTwFVvQhFtM52KK0gOTTPjcTR5qJ04BtyCVNFlKEG0Ptf8gjNkbUtcmogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR4t_K0-fC03JRnYb-Qoq4D_MfOtetJyaR3yBCnvWJ5TEJDCDfj4etCWDHODttvlbgDtoqvctn3cShPCyUjdQxCO5pbGbx7N3NcD5McYfRRq8hoIe-t2ynQDXxKHq4RMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCKe5oyDG-JJTnfb5kXQbnV2t5qfn4k-PnVepIFyPnZKxtqtjTj2JojWt0aV4cGMMjMXjQ0DU7qq4TnWncKW-o1KJcrEfOdyfov0xFHDxr405OTX2DO0KJcbRozjh5thPJvyT8DXnO7L4nlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_yJDthhK_lenJb5ICV-frb-C62aKDssCQcBhcqEU-GQTb8-pk75Pjp-qo33jnu_CocWKJJ8Ub20-6j3hj0KtCjtUjJMm7p2qQsWh5nhMJmb67JMxCf-RoJ5-ry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8Jq6kj3D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=0; FANYI_WORD_SWITCH=0; HISTORY_SWITCH=0; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1574067256,1574067329,1574067444,1574130843; yjs_js_security_passport=d820addb21eab16245d1b57273b370b3db268a96_1574131199_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1574133248; __yjsv5_shitong=1.0_7_3fabb0dfe25a2d6128e827fa77b9a4a06a1c_300_1574133248005_114.240.57.115_f919fc83'
    }
    data = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'simple_means_flag': '3',
        'sign': get_sign(query),
        'token': '58bb207f285efe6bd54ab8dd8557d2fb',
    }
    html = requests.post(url, data=data, headers=headers)
    result = html.json()['trans_result']['data'][0]['dst']
    return result

if __name__ == '__main__':
    query = '加密'
    print(baidu_translate(query))
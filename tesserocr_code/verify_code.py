# -*- coding: utf-8 -*-
# @Author: Lishuo
import time
import re
import json
import execjs
import hashlib
import requests as r
from lxml import etree
import tesserocr
from PIL import Image

def get_code(path):
    image = Image.open(path)  # 读取图片
    image = image.convert('L')  # 图片进行灰度处理
    # image = image.convert('1')  # 自动图片进行二值化处理
    threshold = 127  # 代表二值化阈值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()
    result = tesserocr.image_to_text(image)  # 传入图片对象进行识别
    return result


if __name__ == '__main__':
    print(get_code('CheckCode.jpeg'))
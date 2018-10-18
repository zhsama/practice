#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 005.changeImgSize.py
@Time    : 2018/10/11 20:44
@software: PyCharm

'''
import os
import glob
from PIL import Image


def convertimg(imgFile, outDir, width=128, height=128):
    img = Image.open(imgFile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        new_img.save(os.path.join(outDir, os.path.basename(imgFile)))
    except Exception as e:
        print(e)


for imgFile in glob.glob("C:/Users/QAQ/PycharmProjects/practice/imgs/*.png"):
    convertimg(imgFile, "C:/Users/QAQ/PycharmProjects/practice/change", width=1920, height=1080)

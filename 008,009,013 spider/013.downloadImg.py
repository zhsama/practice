#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 013.downloadImg.py
@Time    : 2018/10/13 16:34
@software: PyCharm

'''
import urllib
import urllib.request
import re
import os


def get_html(url):
    '''
    获取html页面
    :param url:需要访问的页面
    :return: html页面
    '''
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf8')
    return html

def get_img(html):
    '''
    获取图片链接
    :param html:要获取图片的页面html
    :return:需要下载的图片链接列表
    '''
    reg = r'src="(.*?\.jpg)" bdwater='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    i = 0
    path = 'C:\\Users\QAQ\PycharmProjects\practice\downloadImg'
    for imgurl in imglist:
        filename = '%s.jpg'%i
        urllib.request.urlretrieve(imgurl, os.path.join(path,filename))
        i+=1

html = get_html('http://tieba.baidu.com/p/2166231880')
print(get_img(html))
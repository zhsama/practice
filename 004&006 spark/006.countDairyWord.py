#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 006.countDairyWord.py
@Time    : 2018/10/12 21:02
@software: PyCharm

'''
import glob

files = glob.glob('C:/Users/QAQ/PycharmProjects/practice/dairy')

for file in files:
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            line.split(' ')


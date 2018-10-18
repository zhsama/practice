#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : xlsToXML.py
@Time    : 2018/10/15 21:12
@software: PyCharm

'''
import pandas as pd

df = pd.read_excel('city.xlsx')
# print(data)
data = df.to_json(orient='index', force_ascii=False)

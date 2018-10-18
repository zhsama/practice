#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 015.cityToExcel.py
@Time    : 2018/10/13 20:03
@software: PyCharm

'''
import pandas as pd

list = []
with open('city.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('{') or line.startswith('}'):
            pass
        elif line.endswith(','):
            line = line.strip().split(',')
            line = line.pop(0)
            line = line.split(':')
            list.append(line[1])
        else:
            line = line.split(':')
            list.append(line[1])
            # print(list)

df = pd.DataFrame(list)
writer = pd.ExcelWriter('city.xlsx')
df.to_excel(writer)
writer.save()

#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 014.stuToExcel.py
@Time    : 2018/10/13 18:10
@software: PyCharm

'''
import pandas as pd

list = []
with open('students.txt',encoding='utf8') as f:
    for line in f:
        if line.startswith('{') or line.startswith('}'):
            pass
        else:
            line = line.strip().split(':')
            list.append(line[1])
            # print(line)

# print(pd.DataFrame(list))
df = pd.DataFrame(list)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer)
writer.save()
#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : test'.py
@Time    : 2018/10/18 19:34
@software: PyCharm

'''
test = ['fbnq.py', 'fbnq.cmd', 'fbnq.dat', 'countCodeline.py', 'countCodeline.dat', 'countCodeline.cmd']
py = []
for item in test:
    if item.endswith('.py') and item not in py:
        py.append(item)
    else:
        continue

print(py)

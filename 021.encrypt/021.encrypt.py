#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 021.encrypt.py
@Time    : 2018/10/18 16:32
@software: PyCharm

'''
import string
from random import Random
from hashlib import md5


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = string.ascii_letters
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update((pwd + salt).encode("utf-8"))
    return md5_obj.hexdigest()


# 原始密码
pwd = '20141124'
# 随机生成4位salt
salt = create_salt()
# 加密后的密码
md5 = create_md5(pwd, salt)

print('pwd is :', pwd)
print('salt is :', salt)
print(md5)

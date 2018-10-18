#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 001~003.randCode.py
@Time    : 2018/10/11 16:50
@software: PyCharm

'''
import string
import random
import pymysql


class Code():
    code = []

    def __init__(self, length, times):
        self.length = length
        self.times = times

    def rand(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, self.length))

    def rm(self, a):
        '''
        去除list中的重复项
        :param a:传入需要判断是否重复的code
        :return: 不与list重复的code
        '''
        if a in self.code:
            return self.rand()
        else:
            return a

    def loop(self):
        '''
        创建优惠码
        :return: 优惠码列表
        '''
        for i in range(self.times):
            a = self.rand()
            a = self.rm(a)
            self.code.append(a)
        return self.code


if __name__ == '__main__':
    code = Code(length=8, times=200)
    print(code.loop())


# save to mysql
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# cursor = db.cursor()


# save to redis

#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : fbnq.py
@Time    : 2018/10/10 17:26
@software: PyCharm

'''
from time import ctime, sleep
import threading
from time import ctime


class myThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print('end', self.name, 'at:', ctime())


def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x - 1))


def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x - 1))


funcs = [fib, fac, sum]

n = 12


def main():
    nfuncs = range(len(funcs))

    print('*** SINGLE THREAD')

    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('\n*** MULTIPLE THREADS')

    threads = []
    # 给三个方法分别创建进程
    for i in nfuncs:
        t = myThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('all done in', ctime())


if __name__ == '__main__':
    main()

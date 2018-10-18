#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 011.filtWord.py
@Time    : 2018/10/12 21:14
@software: PyCharm

'''


def getFilterwords():
    filterWords = []
    with open('filterwords.txt', 'r', encoding='utf8') as f:
        for word in f:
            word = word.strip()
            filterWords.append(word)
    return filterWords


def checkFilterwords(filtWord, Input):
    for w in filtWord:
        if w == Input:
            print('Freedom')
            return
    print('Human Rights')


if __name__ == '__main__':
    checkFilterwords(getFilterwords(), input())

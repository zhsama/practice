#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 006.py(not spark).py
@Time    : 2018/10/18 17:05
@software: PyCharm

'''
import collections
import re


class mostWord:
    def lists(self, string):
        words = re.findall(r'[a-zA-Z]+\b', string)  # 修改了正则表达式
        return words

    def openFile(self, fileName):
        with open(fileName, 'r') as f:
            article = f.read()
            return article

    def most_word_number(self, wordList):
        wordcount = collections.Counter(wordList)
        top_one = wordcount.most_common(1)
        return top_one


mw = mostWord()
words = mw.openFile('GitHub.txt')
lists = mw.lists(words)
print(mw.most_word_number(lists))

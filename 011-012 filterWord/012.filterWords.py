#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 012.filterWords.py
@Time    : 2018/10/13 16:23
@software: PyCharm

'''
import re


class filterWord:
    def getFilterWord(self, file):
        '''
        获取敏感词文件
        :param file : 敏感词汇总文件名
        :return : 敏感词列表
        '''
        filtWords = []

        with open(file, 'r', encoding='utf8') as f:
            for word in f:
                word = word.strip()
                filtWords.append(word)
        return filtWords

    def gen_patten(self, words):
        '''
        生成对应的正则匹配规则
        :param words : 敏感词列表
        :return : 敏感词正则表达式
        '''
        pattern = ''
        for string in words:
            pattern += string + '|'
        return pattern[:-1]

    def inputReplace(self, pattern):
        '''
        替换输出
        :param pattern: 敏感词正则表达式
        :return: 替换后的输出
        '''
        sentence = input('Please enter a sentence:')
        print(re.sub(pattern, '**', sentence))


fw = filterWord()
wordlist = fw.getFilterWord('filterwords.txt')
wordgen = fw.gen_patten(wordlist)
fw.inputReplace(wordgen)

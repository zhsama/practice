#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 004.countWords.py
@Time    : 2018/10/11 18:57
@software: PyCharm

'''

import os
import shutil
from pyspark import SparkContext

inputPath = 'input.txt'
outputPath = 'result.txt'

sc = SparkContext('local', 'wordcount')

# 读取文件
input = sc.textFile(inputPath)
# 切分单词
words = input.flatMap(lambda line: line.split(' '))
# 转换成键值对并计数
counts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

# 输出结果
counts.foreach(print)

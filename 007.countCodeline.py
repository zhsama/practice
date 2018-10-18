#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 007.countCodeline.py
@Time    : 2018/10/11 20:26
@software: PyCharm

'''
import glob
import os

file = []  # 递归遍历得到的所有文件的集合
pyfile = []  # 其中python文件的集合

g = os.walk("C:/Users/QAQ/PycharmProjects/practice")  # 父文件目录

# 递归遍历项目文件夹中的所有文件
for path, d, filelist in g:
    for filename in filelist:
        if filename not in file:
            file.append(os.path.join(path, filename))

# 获取python文件并添加到列表
for item in file:
    if item not in pyfile and item.endswith('.py'):
        pyfile.append(item)

# files = glob.glob('C:/Users/QAQ/PycharmProjects/practice/*.py')

# 注释行数
comment_lines = 0
# 代码行数
code_lines = 0
# 空行数
blank_lines = 0
# 记录以'''或"""开头的注释位置
start_comment_index = 0
not_comment = True

for file in pyfile[:10]:
    with open(file, 'r', encoding='utf8') as f:
        for index, line in enumerate(f, start=1):
            line = line.strip()

            if not_comment:
                if line.startswith("'''") or line.startswith('"""'):
                    start_comment_index = index
                    not_comment = False
                elif line.startswith("#"):
                    comment_lines += 1
                elif line == "":
                    blank_lines += 1
                else:
                    code_lines += 1
            else:
                if line.endswith("'''") or line.endswith('"""'):
                    not_comment = True
                    comment_lines += index - start_comment_index + 1
                else:
                    pass

print("注释:%d" % comment_lines)
print("空行:%d" % blank_lines)
print("代码:%d" % code_lines)

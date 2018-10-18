#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 016.xls2xml.py
@Time    : 2018/10/15 16:26
@software: PyCharm

'''
import json
import xlsxwriter


class Students:
    def __init__(self, openFileName, saveFileName):
        '''
        :param openFileName: 打开的txt文件名
        :param saveFileName: 保存的json文件名
        '''
        self.saveFileName = saveFileName
        self.openFileName = openFileName

    def txtTojson(self):
        '''
        将txt文件保存为json文件
        :return:
        '''
        with open(self.openFileName, encoding='utf8') as f1:
            data = json.loads(f1.read())
            with open(self.saveFileName, mode='w+', encoding='utf8') as f2:
                json.dump(data, f2, ensure_ascii=False)

    def readJson(self):
        '''
        读取json文件中的内容
        :param fileName: 要读取的文件名
        :return: 文件内容
        '''
        with open(self.saveFileName, mode='r', encoding='utf8') as f:
            return json.load(f)

    def writeToXls(self, jsonFile, xlsName):
        '''
        将读取的json文件内容写入Excel
        :param xlsName: 要保存的Excel文件名
        :param obj: 读取的json内容
        :return:
        '''
        # print(self.readJson())
        workbook = xlsxwriter.Workbook(xlsName)
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0
        for d, x in jsonFile.items():
            worksheet.write(row, col, int(d))
            # print(d)
            # print(x)
            col = col + 1
            for data in x:
                worksheet.write(row, col, data)
                col += 1

            worksheet.write(row, col, '=SUM(C%d:E%d)' % (row + 1, row + 1))
            col = 0
            row += 1
        workbook.close()


if __name__ == '__main__':
    s = Students('students.txt', 'students.json')
    f = s.readJson()
    s.writeToXls(f, 'students.xls')

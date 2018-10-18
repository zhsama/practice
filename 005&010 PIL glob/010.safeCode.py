#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : 010.safeCode.py
@Time    : 2018/10/12 17:31
@software: PyCharm

'''
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class safeCode:
    def __init__(self, font_path, number, size=(100, 30), bgColor=(255, 255, 255),
                 fontColor=(0, 0, 255),
                 lineColor=(255, 0, 0),
                 draw_line=True, line_number=(1, 5)):
        '''
        :param font_path:   字体文件路径
        :param number:      验证码长度
        :param size:        创建的图片大小
        :param bgColor:     背景颜色
        :param fontColor:   字体颜色
        :param lineColor:   干扰线颜色
        :param draw_line:   是否创建干扰线
        :param line_number: 干扰线条数
        '''
        self.font_path = font_path
        self.number = number
        self.size = size
        self.bgColor = bgColor
        self.fontColor = fontColor
        self.lineColor = lineColor
        self.draw_line = draw_line
        self.line_number = line_number

    def gene_text(self):
        '''
        创建验证码的随机字符串
        :return: 随机字符串
        '''
        source = list(string.ascii_letters)
        for i in range(self.number):
            source.append(str(i))
        return ''.join(random.sample(source, self.number))  # number是生成验证码的位数

    def gene_line(self, draw, width, height):
        '''
        创建干扰线
        :param draw:    画布对象
        :param width:  干扰线宽度
        :param height: 干扰线长度
        :return:       干扰线对象
        '''
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=self.lineColor)

    def gene_code(self):
        width, height = self.size  # 宽和高
        image = Image.new('RGBA', (width, height), self.bgColor)  # 创建图片
        font = ImageFont.truetype(self.font_path, 25)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = self.gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)
        draw.text(((width - font_width) / self.number, (height - font_height) / self.number), text,
                  font=font, fill=self.fontColor)  # 填充字符串
        if self.draw_line:
            self.gene_line(draw, width, height)
        image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0),
                                Image.BILINEAR)  # 创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
        image.save('safeCode.png')  # 保存验证码图片


if __name__ == "__main__":
    code = safeCode(font_path='C:/Windows/Fonts/Arial.ttf', number=4)
    code.gene_code()

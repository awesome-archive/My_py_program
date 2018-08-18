﻿# -*- encoding:UTF-8 -*-
"""
This is a test for find the font in ass file
"""
import re
import time
import io
import sys
import os

import wx
from wx import FontEnumerator

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print(time.ctime())

installed_fonts = ['FZZhunYuan-M02',  'Microsoft YaHei'
                   ]

# installed_fonts = ['微软雅黑', '方正综艺简体', '方正隶变简体', '方正小标宋简体', \
#                     '方正卡通简体', '方正粗圆简体', '方正粗宋简体', '方正大黑简体',\
#                     '方正超粗黑简体','方正华隶简体','华文中宋','宋体','德彪钢笔行书字库',\
#                     '方正粗宋_GBK','方正楷体简体','方正静蕾简体','方正大标宋简体','方正超粗黑_GBK',\
#       '方正艺黑简体','方正兰亭特黑简体','方正兰亭特黑长简体','迷你霹雳体'
#       ]

aaa = wx.App(False)
My_fonts1 = wx.FontEnumerator().GetFacenames()


length = len(My_fonts1)
for i in range(length):
    if i < length:
        if '@' in My_fonts1[i]:
            My_fonts1.remove(My_fonts1[i])
            length = len(My_fonts1)

My_fonts2 = os.listdir('C:\\Windows\\Fonts')
for i in range(len(My_fonts2)):
    if '.' in My_fonts2[i]:
        sub_s = My_fonts2[i].find('.')
        My_fonts2[i] = My_fonts2[i][:sub_s]

My_fonts = list(set(My_fonts1+My_fonts2))
My_fonts.extend(installed_fonts)

# print(My_fonts)
# print(os.getcwd())

assFileName = os.listdir(os.getcwd())
length = len(assFileName)
i = 0
while (i < length):
    if i < length:
        if 'ass' not in assFileName[i]:
            assFileName.remove(assFileName[i])
            i -= 1
            length = len(assFileName)
    i += 1


def findFont(fileName):
        try:
            with open(fileName, 'r', encoding='utf-8-sig') as f:
                txt = f.read()
                txt2 = re.findall('fn(.*?)}', txt)
                txt2 = list(set(txt2))
                for i in range(len(txt2)):
                    if '\\' in txt2[i]:
                        sub_s = txt2[i].find('\\')
                        txt2[i] = txt2[i][:sub_s]
                txt2 = list(set(txt2))

                for i in range(len(txt2)):
                    if txt2[i] in My_fonts:
                        print('find', txt2[i])
                    else:
                        print('not find', txt2[i])
                print("\n")

        except UnicodeDecodeError:
            with open(fileName, 'r', encoding='utf-16') as f:
                txt = f.read()
                txt2 = re.findall('fn(.*?)}', txt)
                txt2 = list(set(txt2))
                for i in range(len(txt2)):
                    if '\\' in txt2[i]:
                        sub_s = txt2[i].find('\\')
                        txt2[i] = txt2[i][:sub_s]
                txt2 = list(set(txt2))

                for i in range(len(txt2)):
                    if txt2[i] in My_fonts:
                        print('find', txt2[i])
                    else:
                        print('not find', txt2[i])

                print("\n")

for i in range(len(assFileName)):
    print(assFileName[i])
    findFont(assFileName[i])

a = input("press enter to exit")
# print(txt2)

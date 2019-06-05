#coding=utf-8

import pandas as pd
import numpy as np
from xpinyin import Pinyin

#把需要转拼音的列名称改为'汉字'
path = r'C:\Users\lilinyang\Desktop\pinyin.csv'

p = Pinyin()
a = pd.read_csv(path)
l = a['汉字']
pinyin_list = []
for i in l:
    t = p.get_pinyin(i,'')
    pinyin_list.append(t)

result = pd.Series(pinyin_list)
print(result)
result.to_csv(r'C:\Users\lilinyang\Desktop\pinyin_1.csv')


# -*- coding: utf-8 -*-
#asdf = "TeS"
#print(asdf.lower())

import pandas as pd

col = ['c1', 'c2']
aa = ['c0']
print(aa + col)
raw_data = {'roe':['val1', 'val2'] }
data = pd.DataFrame(raw_data)
data.index = col

data.T.to_csv('test.csv')

data2 = pd.read_csv("test.csv", index_col=0)
print(data2)

data2['c3'] = 'val3'
print(data2)

data2.T.to_csv('test.csv')


data3 = pd.read_csv("test.csv", index_col=0)
print(data3)
# -*- coding: utf-8 -*-
asdf = "TeS"
print(asdf.lower())

from pandas import Series, DataFrame

roe = ['roe1', 'roe2']
bps = ['bps1', 'bps2']

raw_data = {'roe':roe, 'bps':bps}

data = DataFrame(raw_data)
data.index = ['2016','2017']

data2 = DataFrame(raw_data)
data2.index = ['2016','2017']

data = data.T
data2 = data2.T
data.to_csv('test.csv')
data2.to_csv('test.csv',mode='a', header=False)

print(data)

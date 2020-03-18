# -*- coding: utf-8 -*-
from pandas import DataFrame, Series
Table = DataFrame()

aList = ['a','b','c','d']
bList = ['1','2','3','4']
yList = ['2016','2017','2018','2019']

print(yList)
yList.pop(1)
print(yList)

Table['abc1'] = aList 
Table['abc2'] = bList 
Table.index = yList
Table = Table.T
Table.to_csv("test.csv")
    
test = "<babo>345</babo>"
sss1 = test.split(">")
sss2 = sss1[1].split("<")
print(sss2[0])
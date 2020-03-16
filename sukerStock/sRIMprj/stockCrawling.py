import requests as re
from bs4 import BeautifulSoup
from pandas import DataFrame, Series
import numpy as np
import pandas as pd

compInfo_head="https://comp.fnguide.com/svo2/asp/SVD_FinanceRatio.asp?pGB=1&gicode="
compInfo_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
# https://comp.fnguide.com/svo2/asp/SVD_Main.asp?pGB=1&gicode=A151860&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701
#   A151860
# fnGuideUrl_head="https://comp.fnguide.com/svo2/asp/SVD_Main.asp?pGB=1&"
# fnGuideUrl_companyCode="gicode="
# fnGuideUrl_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701"
yearList=["2015/12", "2016/12", "2017/12", "2018/12", "2019/12"]
yearCLE="2019/09"

def crawlingFNGUIDE(companyCode):
    #for code in tickers.keys():
    code = companyCode
    fnGuideUrl = compInfo_head + companyCode + compInfo_tail
    url = re.get(fnGuideUrl)
    url = url.content

    html = BeautifulSoup(url,'html.parser')
    body = html.find('body')

    fn_body = body.find('div',{'class':'fng_body'})
    #종목명 따오기
    compNameSplit1 = fn_body.find('div',{'class':'section ul_corpinfo'})
    compNameSplit2 = compNameSplit1.find('h1',{'id':'giName'})
    companyName = compNameSplit2.contents[0].replace('\xa0',' ')

    #구체적인 DATA를 얻어오는 부분, ROE
    dataSplit1 = fn_body.find('div',{'class':'section ul_de'})
    dataSplit2 = dataSplit1.find('div',{'class':'um_table'})

    #2019/12 실적 유무 및 table의 기준연도 파악을 위해서...
    yearThead = dataSplit2.find('thead')
    allTh = yearThead.find_all('th')

    dataTbody = dataSplit2.find('tbody')
    allTr = dataTbody.find_all('tr')

    Table = DataFrame()

    year_list=[]
    roe_list=[]

    for i in allTh:
        for dateStr in yearList :
            if dateStr in i :
                print(dateStr)
                year_list.append(dateStr)
                break
        
        if yearCLE in i :
            year_list.append(yearCLE)
    
    print(year_list)

    for i in allTr:
        category = i.find('span',{'class':'txt_acd'})
        if category == None:
            continue
   
        category = category.text.strip()
        if category == 'ROE':
            j = i.find_all('td',{'class':'r'})
            print(j)

            for value in j:
                try:
                    temp = float(value.contents[0])
                    print(value.contents[0])
                    roe_list.append(temp)
                except:
                    roe_list.append(0)
    
    print(roe_list)

    Table['ROE'] = roe_list
    Table.index = year_list
    print(Table)
    Table = Table.T
    Table.to_csv('test.csv')


def arrangeTable():
    Table = DataFrame()
    year_list = ['09','10','11','12']
    roe_list = ['a','b','c','d']
    ttt_list = ['1','2','3','4']
    Table['RRR'] = roe_list
    Table['EEE'] = ttt_list
    Table.index = year_list
    
    print(Table)
    Table = Table.T
    Table.to_csv('test.csv')


#crawlingFNGUIDE("A151860")
arrangeTable()

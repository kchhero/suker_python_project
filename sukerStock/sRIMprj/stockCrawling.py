import requests as re
from bs4 import BeautifulSoup
from pandas import DataFrame, Series
import numpy as np
import pandas as pd

class stockCrawling :
    # 재무비율 : ROE
    financeRatio_head="https://comp.fnguide.com/svo2/asp/SVD_FinanceRatio.asp?pGB=1&gicode="
    financeRatio_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
    
    # 투자지표 : BPS
    investIndex_head="https://comp.fnguide.com/svo2/asp/SVD_Invest.asp?pGB=1&gicode="
    investIndex_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
    
    yearList_2019=["2015/12", "2016/12", "2017/12", "2018/12", "2019/12"]
    yearList_2020=["2016/12", "2017/12", "2018/12", "2019/12", "2020/12"]
    yearCLE_2019="2019/09"
    yearCLE_2020="2020/09"
    
    yearList = yearList_2019
    yearCLE = yearCLE_2019
    
    year_list=[]
    roe_list=[]
    bps_list=[]
    companyName=""
    
    def crawlingFNGUIDE_financeRatio(self, companyCode):
        fnGuideUrl = self.financeRatio_head + companyCode + self.financeRatio_tail
        url = re.get(fnGuideUrl)
        url = url.content
    
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
    
        fn_body = body.find('div',{'class':'fng_body'})
        #종목명 따오기
        compNameSplit1 = fn_body.find('div',{'class':'section ul_corpinfo'})
        compNameSplit2 = compNameSplit1.find('h1',{'id':'giName'})
        self.companyName = compNameSplit2.contents[0].replace('\xa0',' ')
    
        #구체적인 DATA를 얻어오는 부분, ROE
        dataSplit1 = fn_body.find('div',{'class':'section ul_de'})
        dataSplit2 = dataSplit1.find('div',{'class':'um_table'})
    
        #2019/12 실적 유무 및 table의 기준연도 파악을 위해서...
        yearThead = dataSplit2.find('thead')
        allTh = yearThead.find_all('th')
    
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
    
        # get year table
        for i in allTh:
            for dateStr in self.yearList :
                if dateStr in i :
                    print(dateStr)
                    self.year_list.append(dateStr)
                    break
            
            if self.yearCLE in i :
                self.year_list.append(self.yearCLE)
        
        #print(year_list)
        
        # get ROE table
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
                        #print(temp)
                        self.roe_list.append(temp)
                    except:
                        self.roe_list.append(0)
                break

        # print(roe_list)
    
    def crawlingFNGUIDE_investIndex(self, companyCode):
        fnGuideUrl = self.investIndex_head + companyCode + self.investIndex_tail
        url = re.get(fnGuideUrl)
        url = url.content
    
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
    
        fn_body = body.find('div',{'class':'fng_body'})

        #구체적인 DATA를 얻어오는 부분, BPS
        dataSplit1 = fn_body.find('div',{'class':'section ul_de'})
        dataSplit2 = dataSplit1.find('div',{'class':'ul_col2wrap pd_t25'})
        dataSplit3 = dataSplit2.find('div',{'class':'um_table'})
    #compBody > div.section.ul_de > div.ul_col2wrap.pd_t25 > div.um_table > table
        print(dataSplit3)
        dataTbody = dataSplit3.find('tbody')
        print(dataTbody)
        allTr = dataTbody.find_all('tr')

        # get BPS table
        for i in allTr:
            category = i.find('span',{'class':'txt_acd'})
            if category == None:
                continue
       
            category = category.text.strip()
            if category == 'BPS':
                j = i.find_all('td',{'class':'r'})
                print(j)
    
                for value in j:
                    try:
                        temp = value.contents[0].replace(',','')
                        print(temp)
                        self.bps_list.append(temp)
                    except:
                        self.bps_list.append(0)
                break

        # print(roe_list)
    
    
    def arrangeTable(self, companyCode):
        Table = DataFrame()
        Table['ROE'] = self.roe_list
        Table['BPS'] = self.bps_list
        Table.index = self.year_list
        Table = Table.T
        Table.to_csv(self.companyName + '_' + companyCode + '.csv')
        
        print(Table)
        Table = Table.T
        Table.to_csv('test.csv')


bbb = stockCrawling()
bbb.crawlingFNGUIDE_financeRatio("A151860")
bbb.crawlingFNGUIDE_investIndex("A151860")
bbb.arrangeTable("A151860")

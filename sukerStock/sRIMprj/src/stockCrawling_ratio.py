# -*- coding: utf-8 -*-

import requests as re
from bs4 import BeautifulSoup

class stockCrawlingRatio :
    # 재무비율 : ROE
    financeRatio_head="https://comp.fnguide.com/svo2/asp/SVD_FinanceRatio.asp?pGB=1&gicode="
    financeRatio_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
    
    # 투자지표 : BPS
    investIndex_head="https://comp.fnguide.com/svo2/asp/SVD_Invest.asp?pGB=1&gicode="
    investIndex_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
    
    yearList_2019=["2015/12", "2016/12", "2017/12", "2018/12", "2019/12"]
    yearList_2020=["2016/12", "2017/12", "2018/12", "2019/12", "2020/12"]
    yearCLE_2019="2019/12"
    yearCLE_2020="2020/09"
    
    yearList = yearList_2019
    yearCLE = yearCLE_2019
    
    companyCode = ""    #종목 코드
    year_list=[]        #결산 연/월 list
    roe_list=[]         #ROE list
    bps_list=[]         #BPS list

    def __init__(self, param):
        self.companyCode = param
    
    def setCompCode(self, code):
        self.companyCode = code
    def getYearList(self) :
        return self.year_list
    def getROEList(self) :
        return self.roe_list
    def getBPSList(self) :
        return self.bps_list
    
    def crawlingFNGUIDE_financeRatioRun(self):
        self.year_list.clear()
        self.roe_list.clear()
        self.bps_list.clear()
        
        fnGuideUrl = self.financeRatio_head + self.companyCode + self.financeRatio_tail
        url = re.get(fnGuideUrl)
        url = url.content
    
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
    
        fn_body = body.find('div',{'class':'fng_body'})
    
        #구체적인 DATA를 얻어오는 부분
        dataSplit1 = fn_body.find('div',{'class':'section ul_de'})
        dataSplit2 = dataSplit1.find('div',{'class':'um_table'})
    
        #---------------------------------------------------------------------
        # 결산 연/월 list
        # 2019/12 실적 유무 및 table의 기준연도 파악을 위해서...
        #---------------------------------------------------------------------
        yearThead = dataSplit2.find('thead')
        allTh = yearThead.find_all('th')
        print("allTh : " + str(allTh))
              
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
        print("allTr : " + str(allTr))
        
        for i in allTh:
            for dateStr in self.yearList :
                if dateStr in i :
                    self.year_list.append(dateStr)
                    print("dateStr = " + str(dateStr))
                    break
            
            # if self.yearCLE in i :
            #     print("i = " + str(i))
            #     self.year_list.append(self.yearCLE)
        
        print("year list = " + str(self.year_list))
        #---------------------------------------------------------------------
        # ROE list
        #---------------------------------------------------------------------
        for i in allTr:
            category = i.find('span',{'class':'txt_acd'})
            if category == None:
                continue
       
            category = category.text.strip()
            if category == 'ROE':
                j = i.find_all('td',{'class':'r'})
                    
                for value in j:
                    try:
                        temp = float(value.contents[0])
                        self.roe_list.append(temp)
                    except:
                        self.roe_list.append(0)
                break

   
    def crawlingFNGUIDE_investIndexRun(self):
        fnGuideUrl = self.investIndex_head + self.companyCode + self.investIndex_tail
        url = re.get(fnGuideUrl)
        url = url.content
    
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
    
        fn_body = body.find('div',{'class':'fng_body'})

        #구체적인 DATA를 얻어오는 부분, BPS
        dataSplit1 = fn_body.find('div',{'class':'section ul_de'})
        dataSplit2 = dataSplit1.find('div',{'class':'ul_col2wrap pd_t25'})
        dataSplit3 = dataSplit2.find('div',{'class':'um_table'})

        dataTbody = dataSplit3.find('tbody')
        allTr = dataTbody.find_all('tr')

        #---------------------------------------------------------------------
        # BPS table
        #---------------------------------------------------------------------
        for i in allTr:
            category = i.find('span',{'class':'txt_acd'})
            if category == None:
                continue
       
            category = category.text.strip()
            if category == 'BPS':
                j = i.find_all('td',{'class':'r'})
    
                for value in j:
                    try:
                        temp = value.contents[0].replace(',','')
                        self.bps_list.append(temp.strip())
                    except:
                        self.bps_list.append(0)
                break

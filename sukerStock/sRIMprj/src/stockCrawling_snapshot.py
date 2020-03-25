# -*- coding: utf-8 -*-
import requests as re
from bs4 import BeautifulSoup

class stockCrawlingSnapshot :
    # snapshot
    snapshot_head="https://comp.fnguide.com/svo2/asp/SVD_Main.asp?pGB=1&gicode="
    snapshot_tail="&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701"
    
    companyCode=""      #종목코드
    companyName=""      #회사명
    currentValue=""     #전일종가
    totalShareCount=""  #총 주식수
    companySelfShareCount=""
    shareHolders_list=[]
    
    def __init__(self, param):
        self.companyCode = param
    
    def setCompCode(self, code):
        self.companyCode = code

    def getCompName(self) :
        return self.companyName
    def getTotalShareCount(self) :
        return self.totalShareCount
    def getCurrentValue(self) :
        return self.currentValue
    def getCompSelfShareCount(self) :
        return self.companySelfShareCount
    def getShareHoldersList(self) :
        return self.shareHolders_list

    def crawlingFNGUIDE_snapshotRun(self):
        fnGuideUrl = self.snapshot_head + self.companyCode + self.snapshot_tail
        url = re.get(fnGuideUrl)
        url = url.content
    
        html = BeautifulSoup(url,'html.parser')
        body = html.find('body')
    
        fn_body = body.find('div',{'class':'fng_body'})

        #종목명 따오기
        compNameSplit1 = fn_body.find('div',{'class':'section ul_corpinfo'})
        compNameSplit2 = compNameSplit1.find('h1',{'id':'giName'})
        self.companyName = compNameSplit2.contents[0].replace('\xa0',' ').strip()
    
        #구체적인 DATA를 얻어오는 부분, ROE
        dataSplit1 = fn_body.find('div',{'class':'section ul_de'})

        #---------------------------------------------------------------------
        # 전일종가
        #---------------------------------------------------------------------
        dataSplit2 = dataSplit1.find('div',{'id':'svdMainGrid1'})
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
        for i in allTr:
            category = i.find('span',{'class':'tcr'})
            if category == None:
                continue

            subCategory = i.find('div')
            if "종가/ 전일대비" in subCategory :
                self.currentValue = i.find('td',{'class':'r'})
                #<td class="r">2440/ <span class="tcr">+255</span></td>
                self.currentValue = str(self.currentValue).split('<td class="r">')[1]
                self.currentValue = self.currentValue.split('/')[0].replace(',','')
                break

        #---------------------------------------------------------------------
        # 총 주식수
        #---------------------------------------------------------------------
        dataSplit2 = dataSplit1.find('div',{'id':'svdMainGrid1'})
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
        for i in allTr:
            category = i.find('span',{'class':'csize'})
            if category == None:
                continue
       
            category = category.text.strip()
            if category == '(보통주/ 우선주)':
                value = i.find('td',{'class':'r'})
                self.totalShareCount = value.contents[0].split('/')[0].replace(',','').strip()
                break
    
        #---------------------------------------------------------------------
        # 자기 주식수
        #---------------------------------------------------------------------
        dataSplit2 = dataSplit1.find('div',{'id':'svdMainGrid5'})
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
        for i in allTr:
            tempTh = i.find('th')
            if tempTh == None:
                continue
            #svdMainGrid5 > table > tbody > tr:nth-child(5) > th
            tempMyShare = str(tempTh.find('div'))
            if '자기주식' in tempMyShare:
                tempMyShare2 = i.find_all('td',{'class':'r'})
                tempMyShare3 = str(tempMyShare2[1]).split(">")
                tempMyShare4 = tempMyShare3[1].split("<")
                if len(tempMyShare4[0]) <= 1 :
                    self.companySelfShareCount = "0"
                else:
                    self.companySelfShareCount = tempMyShare4[0].replace(',','').strip()
                break
            else :
                continue

        #---------------------------------------------------------------------
        # 지배주주지분
        #highlight_D_A > table > tbody > tr:nth-child(10) > th > div
        #---------------------------------------------------------------------
        dataSplit2 = dataSplit1.find('div',{'id':'highlight_D_A'})
        dataTbody = dataSplit2.find('tbody')
        allTr = dataTbody.find_all('tr')
        for i in allTr:
            tempTh = i.find('th')
            if tempTh == None:
                continue
            #svdMainGrid5 > table > tbody > tr:nth-child(5) > th
            tempShareHolders = str(tempTh.find('div'))
            if '지배주주지분' in tempShareHolders:
                tempShareHolders = i.find_all('td',{'class':'r'})
                tempList = tempShareHolders[:4]
                for k in tempList :
                    tempK1 = str(k).split(">")
                    tempK2 = tempK1[1].split("<")
                    tempK3 = tempK2[0].replace(',','')
                    tempK3 = tempK3.replace('\xa0','NOEXIST')
                    self.shareHolders_list.append(tempK3.strip())
                
                break
            else :
                continue

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 17:02:45 2016

@author: choonghyun.jeon
suker stock ver 0.1
"""

from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys

class stockBodyCls :
    refreshTime = ""
    names = []
    codes = []
    buyprices = []
    index = 0
    current_prices = []
    returnRate = []
    totalPurchase = 0
    totalProfit = 0
    numberOfShares = []
    profit = []

    def stockInfoMaking(self) :
        #elf.debugging_()        
        self.current_prices = []
        self.returnRate = []
        self.profit = []
        self.totalProfit = 0
        self.totalPurchase = 0
        for i in range(0,self.index) :            
            self.current_prices.append(self.stockInfoParse(self.codes[i]).replace(',',''))
            self.profit.append((int(self.current_prices[i])-int(self.buyprices[i]))*int(self.numberOfShares[i]))
            returnR = float((int(self.current_prices[i])-int(self.buyprices[i]))*100) / float(self.buyprices[i])
            self.returnRate.append("%0.2f"%returnR)
            self.totalProfit += (int(self.current_prices[i])-int(self.buyprices[i]))*int(self.numberOfShares[i])
            self.totalPurchase += int(self.buyprices[i])*int(self.numberOfShares[i])
            
            
    def stockInfoParse(self,code) :
        FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
        html = urllib.urlopen("http://hyper.moneta.co.kr/fcgi-bin/DelayedCurrPrice10.fcgi?code="+code+"&isReal=true").read()
        html = FromRaw(html)
        soup = BeautifulSoup(html,"html.parser")
        data = soup.find("div", { "class" : "item_info_lt" })
        stockValue = ""
      
        for rr in data.findAll("div"):
            stockValue = rr.findAll("strong")[0].text
            
            #cells2 = rr.findAll("em")[0].text
            diffValues = []
            
            for ss in rr.findAll("em") :
                diffValues.append(ss.text)
                
#            if len(stockValue) > 0 :
#                print unicode(stockValue)
#                print diffValues
#                break
            return stockValue
        
    def loadIni(self) :
        iniFilePath = os.path.dirname(os.path.realpath(__file__)) + self.getDirMark() + "setup.ini"
        if os.path.isfile(iniFilePath) :
            try :
                with open(iniFilePath) as data :
                    for line in data :
                        if len(line) <= 1 :
                            continue

                        tempLine1 = (line.split('>'))[1].strip()
                        if "<*" in line :
                            self.refreshTime = int(tempLine1)
                        else :
                            tempL = tempLine1.split(',')
                            self.names.append(tempL[0])
                            self.codes.append(tempL[1])
                            self.buyprices.append(tempL[2])
                            self.numberOfShares.append(tempL[3])
                            self.index += 1
    
            except IOError :
                print "File open error"
            
    def getDirMark(self) :
        linuxMark = '/'
        winMark = '\\'
        if sys.platform=='linux2' :
            return linuxMark
        else :
            return winMark
            
    def debugging_(self) :
                    #for debugging
        print self.names
        print self.codes
        print self.buyprices
        print self.index
            

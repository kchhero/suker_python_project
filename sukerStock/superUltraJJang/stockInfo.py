# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:00:00 2018

@author: choonghyun.jeon
suker stock info ver 0.9
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys

URL_STOCK_PRE = "http://hyper.moneta.co.kr/fcgi-bin/DelayedCurrPrice10.fcgi?code="
URL_STOCK_POST = "&isReal=true"

class stockInfoCls :
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

    useWindow = {"name" : names, "code" : codes, "buyp" : buyprices, "curp" : current_prices, "pf" : profit}
    
    def stockInfoMaking(self) :
        #elf.debugging_()        
        self.current_prices = []
        self.returnRate = []
        self.profit = []
        self.totalProfit = 0
        self.totalPurchase = 0
        for i in range(0,self.index) :
            self.current_prices.append(self.stockGetCurPrice(self.codes[i]).replace(',',''))
            self.profit.append((int(self.current_prices[i])-int(self.buyprices[i]))*int(self.numberOfShares[i]))
            returnR = float((int(self.current_prices[i])-int(self.buyprices[i]))*100) / float(self.buyprices[i])
            self.returnRate.append("%0.2f"%returnR)
            self.totalProfit += (int(self.current_prices[i])-int(self.buyprices[i]))*int(self.numberOfShares[i])
            self.totalPurchase += int(self.buyprices[i])*int(self.numberOfShares[i])
            
            
    def stockGetCurPrice(self,code) :
#        FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
        print(URL_STOCK_PRE + code + URL_STOCK_POST)
        html = urlopen(URL_STOCK_PRE + code + URL_STOCK_POST).read()
#        html = FromRaw(html)
        soup = BeautifulSoup(html,"html.parser")
        data = soup.find("div", { "class" : "item_info_lt" })
        stockValue = ""
      
        for rr in data.findAll("div"):
            stockValue = rr.findAll("strong")[0].text
            
            #cells2 = rr.findAll("em")[0].text
            diffValues = []
            
            for ss in rr.findAll("em") :
                diffValues.append(ss.text)
                
            return stockValue


    def refresh(self, cls) :
        cls.updateName(1, "test1")
        cls.updateName(2, "test2")
        
    # updateCurrentPrice(self, index, price) :
    # updateBuyPrice(self, index, price) :
        
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
                self.debugging_()
                
            except IOError :
                print ("File open error")
            
    def getDirMark(self) :
        linuxMark = '/'
        winMark = '\\'
        print(sys.platform)
        if sys.platform=='linux2' or sys.platform=='linux' :
            return linuxMark
        else :
            return winMark

    def debugging_(self) :
                    #for debugging
        print(self.names)
        print(self.codes)
        print(self.buyprices)
        print(self.index)
            

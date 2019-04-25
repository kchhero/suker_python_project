# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:00:00 2019

@author: choonghyun.jeon
suker stock info ver 0.1
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys
from colorama import Fore, Style


URL_STOCK_PRE = "http://hyper.moneta.co.kr/fcgi-bin/DelayedCurrPrice10.fcgi?code="
URL_STOCK_POST = "&isReal=true"


class stockInfoCls :
    names = []
    codes = []
    buyprices = []
    index = 0
    current_prices = []
    numberOfShares = []
    profit = []

    maxlength = 0

    def stockInfoMaking(self) :
        self.current_prices = []
        self.profit = []
        for i in range(0, self.index) :
            self.current_prices.append(self.stockGetCurPrice(self.codes[i]).replace(',', ''))
            self.profit.append((int(self.current_prices[i]) - int(self.buyprices[i])) * int(self.numberOfShares[i]))

    def stockGetCurPrice(self, code) :
        html = urlopen(URL_STOCK_PRE + code + URL_STOCK_POST).read()
        soup = BeautifulSoup(html, "html.parser")
        data = soup.find("div", {"class" : "item_info_lt" })
        stockValue = ""

        for rr in data.findAll("div"):
            stockValue = rr.findAll("strong")[0].text
            diffValues = []

            for ss in rr.findAll("em") :
                diffValues.append(ss.text)

            return stockValue

    def refresh(self) :
        temp = ""
        maxSpacing = 40
        for i in range(0, self.index) :
            temp = self.names[i] + "|" + self.codes[i] + " | "
            _spacing = maxSpacing - len(temp)
            if _spacing < 1 :
                _spacing = 1                

            print(Style.RESET_ALL + "--------------------------------------------------------------------------------------")
            if self.current_prices[i] > self.buyprices[i] :
                print(temp + ' ' * _spacing
                      + Fore.RED + 'current : {:,}'.format(int(self.current_prices[i]))
                      + Fore.YELLOW + '  buy : {:,}'.format(int(self.buyprices[i]))
                      + Style.RESET_ALL + '  numOfShares : {:,}'.format(int(self.numberOfShares[i])))
            else :
                print(temp + ' ' * _spacing
                      + Fore.BLUE + 'current : {:,}'.format(int(self.current_prices[i]))
                      + Fore.YELLOW + '  buy : {:,}'.format(int(self.buyprices[i]))
                      + Style.RESET_ALL + '  numOfShares : {:,}'.format(int(self.numberOfShares[i])))

            if self.profit[i] > 0 :
                print(Fore.RED + 'profit : {:,}'.format(self.profit[i]))
            else :
                print(Fore.BLUE + 'profit : {:,}'.format(self.profit[i]))

        print(Style.RESET_ALL + "--------------------------------------------------------------------------------------")

    def loadIni(self) :
        iniFilePath = os.path.dirname(os.path.realpath(__file__)) + self.getDirMark() + "setup.ini"
        if os.path.isfile(iniFilePath) :
            try :
                with open(iniFilePath) as data :
                    for line in data :
                        if len(line) <= 1 :
                            continue

                        tempLine1 = (line.split('>'))[1].strip()
                        tempL = tempLine1.split(',')
                        self.names.append(tempL[0])
                        self.codes.append(tempL[1])
                        self.buyprices.append(tempL[2])
                        self.numberOfShares.append(tempL[3])
                        self.index += 1

            except IOError :
                print ("File open error")

    def getDirMark(self) :
        linuxMark = '/'
        winMark = '\\'
        if sys.platform == 'linux2' or sys.platform == 'linux' :
            return linuxMark
        else :
            return winMark

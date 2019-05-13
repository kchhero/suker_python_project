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
    up_down = []

    maxlength = 0

    def stockInfoMaking(self) :
        self.current_prices = []
        self.profit = []
        tempLocalTuple = ()
        for i in range(0, self.index) :
            tempLocalTuple = self.stockGetCurPrice(self.codes[i])
            self.current_prices.append(tempLocalTuple[0].replace(',', ''))
            self.up_down.append(tempLocalTuple[1])
            self.profit.append((int(self.current_prices[i]) - int(self.buyprices[i])) * int(self.numberOfShares[i]))

    def stockGetCurPrice(self, code) :
        html = urlopen(URL_STOCK_PRE + code + URL_STOCK_POST).read()
        soup = BeautifulSoup(html, "html.parser")
        data = soup.find("div", {"class" : "item_info_lt" })
        stockValue = ""

        for rr in data.findAll("div"):
            stockValue = rr.findAll("strong")[0].text
            # diffValues = []
            up_down = ""

            for ss in rr.findAll("em") :
                if "%" in ss.text :
                    # diffValues.append(ss.text)
                    up_down = ss.text

            return (stockValue, up_down)

    def refresh(self) :
        _name = ""
        maxSpacing = 30
        maxSpacing2 = 25

        for i in range(0, self.index) :
            _name = self.names[i] + "|" + self.codes[i] + " | "

            print(Style.RESET_ALL + "---------------------------------------------------------------------------------------------------------------")
            _spacing = maxSpacing - len(_name)
            if _spacing < 1 :
                _spacing = 1

            # profit
            if self.profit[i] > 0 :
                print(_name + ' ' * _spacing + Fore.RED + 'profit : {:,}'.format(self.profit[i]), end='', flush=True)
            else :
                print(_name + ' ' * _spacing + Fore.BLUE + 'profit : {:,}'.format(self.profit[i]), end='', flush=True)

            _spacing = maxSpacing2 - len('profit : {:,}'.format(self.profit[i]))

            if _spacing > 2 :
                _spacing -= 2

            # up_down
            if '-' in self.up_down[i] :
                print(' ' * _spacing + Fore.BLUE + self.up_down[i], end='', flush=True)
            else :
                print(' ' * _spacing + Fore.RED + self.up_down[i], end='', flush=True)

            # more infomation
            if self.current_prices[i] > self.buyprices[i] :
                print('   '
                      + Fore.RED + 'current : {:,}'.format(int(self.current_prices[i]))
                      + Fore.YELLOW + '  buy : {:,}'.format(int(self.buyprices[i]))
                      + Style.RESET_ALL + '  numOfShares : {:,}'.format(int(self.numberOfShares[i])))
            else :
                print('   '
                      + Fore.BLUE + 'current : {:,}'.format(int(self.current_prices[i]))
                      + Fore.YELLOW + '  buy : {:,}'.format(int(self.buyprices[i]))
                      + Style.RESET_ALL + '  numOfShares : {:,}'.format(int(self.numberOfShares[i])))

        print(Style.RESET_ALL + "---------------------------------------------------------------------------------------------------------------")

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

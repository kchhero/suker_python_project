# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:00:00 2020

@author: choonghyun.jeon
suker stock S-RIM ver 0.1
"""
import sys
from stockCrawling import crawlingFNGUIDE

def main(args):
    value = {'class': ['r', 'cle']}
    print(value['class'])
    print(len(value['class']))
    #args[0] # 종목 code
    #if len(args) < 1 :
    #    return # display usage

    # print("S-SIM Main Run - 종목 코드 : " + args[0])
    # ret = SQL open and search code value
    # if ret == 1 --> SQL search success (exist)
    #    if isDoUpdate? yes
    #crawlingFNGUIDE("A151860")
    #         ret = Crowling with code at fnguide
    #    else
    #         display SRIM values in param (true)
    # else --> SQL search fail (not exist)
    #    ret = crowling with code at fnguide
    #
    # if ret == 1 : # crowling success
    #    ret = calculate SRIM
    #    ret = save in SQL, SRIM and stock informations
    #    if ret != 1 : 
    #        display(ret)
    # else : # crowling fail
    #    display fail reason and exit


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
    # infoCls = stockInfoCls()
    # infoCls.loadIni()
    # infoCls.stockInfoMaking()
    # infoCls.refresh()

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:00:00 2020

@author: choonghyun.jeon
suker stock S-RIM ver 0.1
"""
import sys
from stockCrawling_snapshot import stockCrawlingSnapshot as sCS
from stockCrawling_ratio import stockCrawlingRatio as sCR
from pandas import DataFrame

def tableSetup(totalShareCnt, companySelfShareCnt, yearList, roeList, bpsList, shareHoldersList, compName, compCode):
    Table = DataFrame()
    Table['ROE'] = roeList
    Table['BPS'] = bpsList
    Table['shareHolders'] = shareHoldersList
    Table.index = yearList
    Table = Table.T
    Table.to_csv(compName.replace(' ','_') + "_" + compCode + ".csv")

    
def updateInfo(compCode) :
    #---------------------------------------------------------------------
    # class 초기화
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls = sCS(compCode)
    stockCrawlRatioCls = sCR(compCode)
    
    #---------------------------------------------------------------------
    # 종목명, 총 주식수, 자기주식수, 지배주주지분
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls.crawlingFNGUIDE_snapshotRun()
    compName = stockCrawlSnapshotCls.getCompName()
    totalShareCnt = stockCrawlSnapshotCls.getTotalShareCount()
    compSelfShareCnt = stockCrawlSnapshotCls.getCompSelfShareCount()
    shareHoldersList = stockCrawlSnapshotCls.getShareHoldersList()
    
    #---------------------------------------------------------------------
    # 결산 연/월, ROE, BPS
    #---------------------------------------------------------------------
    stockCrawlRatioCls.crawlingFNGUIDE_financeRatioRun()
    stockCrawlRatioCls.crawlingFNGUIDE_investIndexRun()
    yearList = stockCrawlRatioCls.getYearList()
    if len(yearList) == 5 :
        yearList.pop(0)
    roeList = stockCrawlRatioCls.getROEList()
    if len(roeList) == 5 :
        roeList.pop(0)
    bpsList = stockCrawlRatioCls.getBPSList()    
    if len(bpsList) == 5 :
        bpsList.pop(0)
    
    tableSetup(totalShareCnt, compSelfShareCnt, yearList, roeList, bpsList, shareHoldersList, compName, compCode)
    

def main(args):
    #---------------------------------------------------------------------
    # args[0] # 종목 code
    #---------------------------------------------------------------------
    if len(args) < 1 :
        print("args fail!")
        return # display usage

    print("S-SIM Main Run - 종목 코드 : " + args[0])
    
    #---------------------------------------------------------------------
    # DB searching
    # ret = SQL open and search code value
    #---------------------------------------------------------------------
    # if ret == 1 --> SQL search success (exist)
    #    if isDoUpdate? yes
    updateInfo(args[0])
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
    main(["A151860",""])
    # infoCls = stockInfoCls()
    # infoCls.loadIni()
    # infoCls.stockInfoMaking()
    # infoCls.refresh()

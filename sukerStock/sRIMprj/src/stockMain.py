# -*- coding: utf-8 -*-

"""
Created on Tue Mar 16 14:00:00 2020

@author: choonghyun.jeon
suker stock S-RIM ver 0.1
"""
import sys
from stockCrawling_snapshot import stockCrawlingSnapshot as sCS
from stockCrawling_ratio import stockCrawlingRatio as sCR
from stockCrawling_database import stockCrawlingDB as sCDB
from stockCrawling_display import stockCrawlingDisplay as sCDP
import stockConfig
from pathlib import Path

def updateInfo(compCode) :
    #---------------------------------------------------------------------
    # class 초기화
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls = sCS(compCode)
    stockCrawlRatioCls = sCR(compCode)
    stockCrawlDBCls = sCDB()
    
    #---------------------------------------------------------------------
    # 종목명, 총 주식수, 자기주식수, 지배주주지분
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls.crawlingFNGUIDE_snapshotRun()
    compName = stockCrawlSnapshotCls.getCompName()
    totalShareCnt = stockCrawlSnapshotCls.getTotalShareCount()
    currentValue = stockCrawlSnapshotCls.getCurrentValue()
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
    
    stockCrawlDBCls.csvUpdate(currentValue, totalShareCnt, compSelfShareCnt,
                               yearList, roeList, bpsList, shareHoldersList,
                               compName, compCode)

    return 0

def main(args):
    #---------------------------------------------------------------------
    # args[0] # 종목 code
    #---------------------------------------------------------------------
    if len(args) < 2 :
        print("args fail!")
        return # display usage

    print("S-SIM Main Run - 종목 코드 : " + args[0] + " need Update? : " + args[1])
    
    #---------------------------------------------------------------------
    # class 초기화
    #---------------------------------------------------------------------
    stockCrawlDisplayCls = sCDP()

    #---------------------------------------------------------------------
    # DB searching
    # ret = SQL open and search code value
    #---------------------------------------------------------------------
    compCode = ""
    csvFileList = []
    #openFilePathName = ""
    isNeedUpdate = ""
    
    compCode = args[0]    
    if args[1].lower() == "yes":
        isNeedUpdate = True
    else:
        isNeedUpdate = False

    searchFileCnt = 0
    for path in Path('.').rglob('../csv/*.csv'):
        if compCode in path.name :
            print("found : " + "../csv/" + path.name)
            csvFileList.append("../csv/" + path.name)
            #openFilePathName = path.name
            searchFileCnt += 1
            if searchFileCnt == 2 :
                break;

    if len(csvFileList) == 2 :              # CSV search success (exist)
        if isNeedUpdate :
            ret = updateInfo(compCode)      # Crowling with code at fnguide
            
        else:
            ret = stockCrawlDisplayCls.readAndShowInfo(csvFileList)  # display SRIM values in param (true)
    else :
        if isNeedUpdate :                   # CSV search fail (not exist)
            ret = updateInfo(compCode)      # Crowling with code at fnguide
        else :
            print("Really?, nothing to do")
            return
        
    print("All Success!")

if __name__ == "__main__":
    args = sys.argv[1:]
    #main(args)
    ret = main(["A178320","yes"])
    if ret == 0 :
        pass
    elif ret == stockConfig.FAIL_UPDATE :
        pass 
    elif ret == stockConfig.FAIL_CALCULATE :
        pass
    elif ret == stockConfig.FAIL_CSV_SAVE :
        pass
    elif ret == stockConfig.FAIL_CSV_READ :
        pass
    else :
        pass  # unknown error
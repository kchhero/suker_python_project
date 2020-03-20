# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:00:00 2020

@author: choonghyun.jeon
suker stock S-RIM ver 0.1
"""
import sys
from stockCrawling_snapshot import stockCrawlingSnapshot as sCS
from stockCrawling_ratio import stockCrawlingRatio as sCR
from stockCrawling_database import stockCrawlingDB as sCD
from pathlib import Path


def updateInfo(compCode) :
    #---------------------------------------------------------------------
    # class 초기화
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls = sCS(compCode)
    stockCrawlRatioCls = sCR(compCode)
    stockCrawlDBCls = sCD()
    
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
    
    stockCrawlDBCls.tableSetup(totalShareCnt, compSelfShareCnt, yearList, roeList, bpsList, shareHoldersList, compName, compCode)

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
    stockCrawlDBCls = sCD()
    
    #---------------------------------------------------------------------
    # DB searching
    # ret = SQL open and search code value
    #---------------------------------------------------------------------
    compCode = ""
    openFilePathName = ""
    isNeedUpdate = ""
    
    compCode = args[0]    
    if args[1].lower() == "yes":
        isNeedUpdate = True
    else:
        isNeedUpdate = False

    for path in Path('.').rglob('*.csv'):
        if compCode in path.name :
            print("found : " + path.name)
            openFilePathName = path.name

    if len(openFilePathName) > 1 :         # CSV search success (exist)
        if isNeedUpdate :
            ret = updateInfo(compCode)      # Crowling with code at fnguide
            if ret != 0:
                return ret                 # update Fail
            ret = stockCrawlDBCls.calculateAndSaveSRIMInfo(stockCrawlDBCls, openFilePathName)
        else:
            ret = stockCrawlDBCls.readAndShowInfo(stockCrawlDBCls, openFilePathName)  # display SRIM values in param (true)
    else :                                 # CSV search fail (not exist)
        ret = updateInfo(compCode)          # Crowling with code at fnguide
            
    if ret == 0 : # crowling success or already success
        ret = stockCrawlDBCls.calculateAndSaveSRIMInfo(stockCrawlDBCls, openFilePathName)
        if ret != 0 : 
            return ret                     # calculate Fail Display
    else:
        return ret
        
    print("All Success!")

if __name__ == "__main__":
    args = sys.argv[1:]
    #main(args)
    ret = main(["A151860","yes"])
    if ret == 0 :
        pass
    elif ret == FAIL_UPDATE :
        pass 
    elif ret == FAIL_CALCULATE :
        pass
    elif ret == FAIL_CSV_SAVE :
        pass
    elif ret == FAIL_CSV_READ :
        pass
    else :
        pass  # unknown error
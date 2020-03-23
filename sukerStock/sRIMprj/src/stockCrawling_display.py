# -*- coding: utf-8 -*-

import pandas as pd
import stockConfig as sC

class stockCrawlingDisplay :
    compCode = ""
    
    def __init__(self) :
        pass

    def readAndShowInfo(self, csvFileList) :
        _data_ = ""
        _snapshot_ = ""
        for i in csvFileList :
            if sC.FILE_DELIMETER_DATA in i :
                _data_ = pd.read_csv(i, index_col=0)
                #print(_data_)
            if sC.FILE_DELIMETER_SNAPSHOT in i :
                _snapshot_ = pd.read_csv(i)
                #print(_snapshot_)
        
        print("--------------------------------------------")
        print("종 목 명 : " + str(_snapshot_[sC.T_COMPANY_NAME][0]))
        print("종목코드 : " + str(_snapshot_[sC.T_COMPANY_CODE][0]))
        print("어제종가 : " + str(_snapshot_[sC.T_SHARE_PRICE][0]))
        print("총주식수 : " + str(_snapshot_[sC.T_TOTAL_SHARE][0]))
        print("자기주식수 : " + str(_snapshot_[sC.T_SELF_SHARE][0]))
        print("--------------------------------------------")
        print("연결/연도별 지표")
        print("--------------------------------------------")
        print(_data_)
        print("--------------------------------------------")            
        
#test = stockCrawlingDisplay()
#test.readAndShowInfo(["../csv/KG_ETS_A151860_data_.csv","../csv/KG_ETS_A151860_snapshot_.csv"])
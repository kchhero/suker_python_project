# -*- coding: utf-8 -*-

import pandas as pd
import stockConfig as sC

class stockCrawlingDB :
    compCode = ""
    
    def __init__(self) :
        pass
    
    def tableSetup(self, currentValue, totalShareCnt, companySelfShareCnt,
                   yearList, roeList, bpsList, shareHoldersList,
                   compName, compCode):
        csvFileName = compName.replace(' ','_') + "_" + compCode
        csvFileNameExt = ".csv"

        # 종목명, 종목코드, 총 주싟, 자기 주식수 table 정리 및 저장
        tempList = [sC.T_COMPANY_NAME, sC.T_COMPANY_CODE, sC.T_SHARE_PRICE, sC.T_TOTAL_SHARE, sC.T_SELF_SHARE]
        raw_data = {'':[compName, compCode, currentValue, totalShareCnt, companySelfShareCnt]}
        data = pd.DataFrame(raw_data)
        data.index = tempList
        data.T.to_csv('../csv/' + csvFileName + sC.FILE_DELIMETER_SNAPSHOT + csvFileNameExt)
    
        # ROE, BPS, 지배주주지분  table 정리 및 저장
        raw_data2 = {sC.T_ROE:roeList,
                     sC.T_BPS:bpsList,
                     sC.T_SHARE_HOLDERS:shareHoldersList}
        data2 = pd.DataFrame(raw_data2)
        data2.index = yearList
        data2.T.to_csv('../csv/' + csvFileName + sC.FILE_DELIMETER_DATA + csvFileNameExt)


    def calculateAndSaveSRIMInfo(self, csvFileList) :
        _data_ = ""
        _snapshot_ = ""
        snapshotFileName = ""

        for i in csvFileList :
            if sC.FILE_DELIMETER_DATA in i :
                _data_ = pd.read_csv(i, index_col=0)
                #print(_data_)
            if sC.FILE_DELIMETER_SNAPSHOT in i :
                _snapshot_ = pd.read_csv(i)
                snapshotFileName = i
                #print(_snapshot_)
        
        col0Name = _data_.columns[0]  #2016/12
        col1Name = _data_.columns[1]  #2017/12
        col2Name = _data_.columns[2]  #2018/12
        col3Name = _data_.columns[3]  #2019/09 or 2019/12
        lastColName = col3Name

        #ROW의 순서... 중요...
        _ROE_ = 0
        _SHOLD_ = 2
        #---------------------------------------------------------------------
        #주식수 = 총주식수 - 자기주식수
        #---------------------------------------------------------------------
        shareCnt = int(_snapshot_[sC.T_TOTAL_SHARE][0]) - int(_snapshot_[sC.T_SELF_SHARE][0])

        #---------------------------------------------------------------------
        #초과이익 = 지배주주지분 * (예상 ROE - 기대 수익률)
        #---------------------------------------------------------------------
        lastShareHolder = _data_[lastColName][_SHOLD_]
        if lastShareHolder == "NOEXIST" :
            lastShareHolder = int(_data_[col2Name][_SHOLD_]) #2018/12
        lastShareHolder *= 100000000                         #단위 조절, 억
        
        tempROE = float(_data_[col0Name][_ROE_]) * float(sC.CALC_ROE_WEIGHT0) + \
                  float(_data_[col1Name][_ROE_]) * float(sC.CALC_ROE_WEIGHT1) + \
                  float(_data_[col2Name][_ROE_]) * float(sC.CALC_ROE_WEIGHT2) + \
                  float(_data_[col3Name][_ROE_]) * float(sC.CALC_ROE_WEIGHT3)
        expectedROE = float(tempROE) / float(sC.CALC_ROE_WEIGHT_SUM)
        expectedProfitRatio = sC.EXPECTED_PROFIT_RATIO
        overProfit = lastShareHolder * (expectedROE - expectedProfitRatio) / 100

        #---------------------------------------------------------------------
        #기업가치(지속) = 지배주주지분 + 초과이익 / 기대수익률
        #---------------------------------------------------------------------
        compValueConst = int(lastShareHolder + overProfit / expectedProfitRatio)
        
        #---------------------------------------------------------------------
        #sRIM          = 기업가지(지속) / 주식수
        sRIM = int(compValueConst / shareCnt)
        
        #기업가치(w90) = 지배주주 지분 + 초과이익 * (0.9 / (1 + 기대수익율 - 0.9))
        #sRIM_w90     = 기업가치(w90) / 주식수
        compValueW90 = int(lastShareHolder + overProfit * (0.9 / (1 + expectedProfitRatio - 0.9)))
        sRIM_w90 = int(compValueW90 / shareCnt)
        
        #기업가치(w80) = 지배주주 지분 + 초과이익 * (0.8 / (1 + 기대수익율 - 0.8))
        #sRIM_w80     = 기업가치(w80) / 주식수
        compValueW90 = int(lastShareHolder + overProfit * (0.8 / (1 + expectedProfitRatio - 0.8)))
        sRIM_w80 = int(compValueW90 / shareCnt)
        #---------------------------------------------------------------------
        
        print("-----------Calculating End-----------")
        print("current Price : %d"%int(_snapshot_[sC.T_SHARE_PRICE][0]))
        print("sRIM    : %d"%sRIM)
        print("sRIM w90: %d"%sRIM_w90)
        print("sRIM w80: %d"%sRIM_w80)
        print("-------------------------------------")
        
        
        self.saveSRIM(_snapshot_, sRIM, sRIM_w90, sRIM_w80, snapshotFileName)


    def saveSRIM(self, _snapshot_, sRIM, sRIM_w90, sRIM_w80, snapshotFileName) :
        # sRIM, sRIM_w90, sRIM_w80
        _snapshot_['sRIM'] = str(sRIM)
        _snapshot_['sRIM_w90'] = str(sRIM_w90)
        _snapshot_['sRIM_w80'] = str(sRIM_w80)
        _snapshot_.T.to_csv(snapshotFileName)


#test = stockCrawlingDB()
#test.calculateAndSaveSRIMInfo(["../csv/KG_ETS_A151860_data_.csv","../csv/KG_ETS_A151860_snapshot_.csv"])
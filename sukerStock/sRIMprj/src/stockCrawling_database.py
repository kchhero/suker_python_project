# -*- coding: utf-8 -*-

import pandas as pd
import stockConfig as sC

class stockCrawlingDB :
    compCode = ""
    
    def __init__(self) :
        pass
    
    def csvUpdate(self, currentValue, totalShareCnt, companySelfShareCnt,
                   yearList, roeList, bpsList, shareHoldersList,
                   compName, compCode):
        csvFileName = compName.replace(' ','_') + "_" + compCode
        csvFileNameExt = ".csv"

        #ROW의 순서... 중요...
        _ROE_ = 0
        _SHOLD_ = 2
        #---------------------------------------------------------------------
        #주식수 = 총주식수 - 자기주식수
        #---------------------------------------------------------------------
        shareCnt = int(totalShareCnt) - int(companySelfShareCnt)

        #---------------------------------------------------------------------
        #초과이익 = 지배주주지분 * (예상 ROE - 기대 수익률)
        #---------------------------------------------------------------------
        lastShareHolder = shareHoldersList[-1]
        if lastShareHolder == "NOEXIST" :
            lastShareHolder = int(shareHoldersList[-2]) #2018/12
        lastShareHolder *= 100000000                         #단위 조절, 억
        
        tempROE = float(roeList[0]) * float(sC.CALC_ROE_WEIGHT0) + \
                  float(roeList[1]) * float(sC.CALC_ROE_WEIGHT1) + \
                  float(roeList[2]) * float(sC.CALC_ROE_WEIGHT2) + \
                  float(roeList[3]) * float(sC.CALC_ROE_WEIGHT3)
        expectedROE = float(float(tempROE) / float(sC.CALC_ROE_WEIGHT_SUM) / 100.0)
        expectedProfitRatio = float(sC.EXPECTED_PROFIT_RATIO / 100.0)
        overProfit = lastShareHolder * (expectedROE - expectedProfitRatio)

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
        print("current Price : %d"%int(currentValue))
        print("sRIM    : %d"%sRIM)
        print("sRIM w90: %d"%sRIM_w90)
        print("sRIM w80: %d"%sRIM_w80)
        print("-------------------------------------")

        # 종목명, 종목코드, 총 주싟, 자기 주식수 table 정리 및 저장
        tempList = [sC.T_COMPANY_NAME, sC.T_COMPANY_CODE, sC.T_SHARE_PRICE, sC.T_TOTAL_SHARE, sC.T_SELF_SHARE, sC.T_SRIM, sC.T_SRIM90, sC.T_SRIM80]
        raw_snapshot_ = {'':[compName, compCode, currentValue, totalShareCnt, companySelfShareCnt, str(sRIM), str(sRIM_w90), str(sRIM_w80)]}
        _snapshot_ = pd.DataFrame(raw_snapshot_)
        _snapshot_.index = tempList
        _snapshot_.T.to_csv('../csv/' + csvFileName + sC.FILE_DELIMETER_SNAPSHOT + csvFileNameExt)
    
        # ROE, BPS, 지배주주지분  table 정리 및 저장
        raw_data_ = {sC.T_ROE:roeList,
                     sC.T_BPS:bpsList,
                     sC.T_SHARE_HOLDERS:shareHoldersList}
        _data_ = pd.DataFrame(raw_data_)
        _data_.index = yearList

        _data_.T.to_csv('../csv/' + csvFileName + sC.FILE_DELIMETER_DATA + csvFileNameExt)
        
        # sRIM, sRIM_w90, sRIM_w80
        #_snapshot_['sRIM'] = str(sRIM)
        #_snapshot_['sRIM_w90'] = str(sRIM_w90)
        #_snapshot_['sRIM_w80'] = str(sRIM_w80)



#test = stockCrawlingDB()
#test.calculateAndSaveSRIMInfo(["../csv/KG_ETS_A151860_data_.csv","../csv/KG_ETS_A151860_snapshot_.csv"])
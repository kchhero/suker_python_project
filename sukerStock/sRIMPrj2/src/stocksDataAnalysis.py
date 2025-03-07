# -*- coding: utf-8 -*-
from pathlib import Path
from .stockConfig import stockCrawlingCONFIG as sConfig
import ast
import pandas as pd # type: ignore

class stockDataAnalysis :
    One_hundred_million = int(100000000)
    One_thousand = int(1000)
    
    def __init__(self) :
        pass
    
    def sRIM(self, marketType, stockCode):
        folderPath = ""
        
        if marketType == "Y" or marketType == "y":
            folderPath = Path(sConfig.KOSPI_REFINED_PATH_NAME)
        elif marketType == "K" or marketType == "k":
            folderPath = Path(sConfig.KOSDAQ_REFINED_PATH_NAME)
        else:
            print("Market Type is Strange")
            exit()

        filePath = next(folderPath.glob(f"stockcode_{stockCode}*.txt"), None)
        
        company_name = filePath.name.split("_")[2]

        z_list_years = []
        old_z_list_years = []
        #자사주, 단위 주주
        a_self_stockNum = 0
        #발생주식수, 단위 천주
        b_total_stockNum = 1
        #지배주주지분, 단위 억원
        c_controlling_interest = 1
        #ROE
        d_list_ROE = []
        old_d_list_ROE = []
        #PER
        e_list_PER = []
        old_e_list_PER = []
        #PBR
        f_list_PBR = []
        old_f_list_PBR = []
        #EPS
        g_list_EPS = []
        old_g_list_EPS = []
        
        print(">>>>>>>>>>>>>>>>>>>>------------<<<<<<<<<<<<<<<<<<<")
        print("    %s     기준연도 2024/12"%company_name)     
        print(">>>>>>>>>>>>>>>>>>>>------------<<<<<<<<<<<<<<<<<<<")
        
        #기준 list size
        latest_year_index = 5
        with filePath.open("r", encoding="utf-8") as f:
            for line in f:
                temp = line.strip()
                temp = temp.split("\t")
                if "IFRS(연결)" in line:
                    converted_list = ast.literal_eval(temp[1])                    
                    old_z_list_years = converted_list[:] #converted_list[start_index:latest_index+1]
                    print("years : ", z_list_years)                    

                elif "발행주식수" in line:
                    converted_list = ast.literal_eval(temp[1])
                    temp2 = int(converted_list[-1])
                    b_total_stockNum = int(temp2) * self.One_thousand                                        
                    print("발행주식수(최신) : ", format(b_total_stockNum, ',d'))

                elif "자사주" in line:
                    a_self_stockNum = int(temp[1])
                    print("자사주 : ", format(a_self_stockNum, ',d'))
                    
                elif "지배주주지분" in line:
                    converted_list = ast.literal_eval(temp[1])
                    temp = converted_list[-1]
                    c_controlling_interest = int(temp) * self.One_hundred_million
                    print("지배주주지분 : ", format(c_controlling_interest, ',d'))
                    
                elif "ROE" in line:                    
                    converted_list = ast.literal_eval(temp[1])
                    old_d_list_ROE = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in converted_list[:]]                    
                    
                elif "PER" in line:
                    converted_list = ast.literal_eval(temp[1])
                    old_e_list_PER = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in converted_list[:]]
                    
                elif "PBR" in line:
                    converted_list = ast.literal_eval(temp[1])
                    old_f_list_PBR = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in converted_list[:]]
                    
                elif "EPS" in line:
                    converted_list = ast.literal_eval(temp[1])                    
                    old_g_list_EPS = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in converted_list[:]]

        # z_list_years        
        latest_year_index = next((i for i, item in enumerate(old_z_list_years) if sConfig.LATEST_YEAR in item), -1)
        if latest_year_index == -1:
            print("not found ", sConfig.LATEST_YEAR)
            return

        while True:
            print("Validation Check ...")
            print("IFRS(연결) 최신연도 Set : ", old_z_list_years[latest_year_index])
            
            z_list_years = old_z_list_years[:latest_year_index+1]
            d_list_ROE = old_d_list_ROE[:latest_year_index+1]
            e_list_PER = old_e_list_PER[:latest_year_index+1]
            f_list_PBR = old_f_list_PBR[:latest_year_index+1]
            g_list_EPS = old_g_list_EPS[:latest_year_index+1]
            
            if d_list_ROE[-1] == 0.0 or g_list_EPS[-1] == 0.0 :
                print("최신 자료중 ROE 또는 EPS 값이 없는 경우가 있습니다.")                
                print("IFRS(연결) 최신연도를 변경합니다.")
                latest_year_index -= 1
            else:
                break
        
        print("Years : ", z_list_years)        
        print("ROE : ", d_list_ROE)
        print("PER : ", e_list_PER)
        print("PBR : ", f_list_PBR)
        print("EPS : ", g_list_EPS)
        
        #validate check
        if c_controlling_interest == 1:
            print("지배주주지분 값이 이상하거나 없습니다.")  
            return

        #---------------------------------------------------------------------
        #주식수 = 발행주식수[-1] - 자사주
        #---------------------------------------------------------------------
        shareCnt = int(b_total_stockNum) - int(a_self_stockNum)
        print("주식수 : ", format(shareCnt, ',d'))
        
        #---------------------------------------------------------------------
        #초과이익 = 지배주주지분 * (예상 ROE - 기대 수익률)
        #---------------------------------------------------------------------        
        tempROE = float(d_list_ROE[0]) * float(sConfig.CALC_ROE_WEIGHT0) + \
                  float(d_list_ROE[1]) * float(sConfig.CALC_ROE_WEIGHT1) + \
                  float(d_list_ROE[2]) * float(sConfig.CALC_ROE_WEIGHT2)

        expectedROE = float(float(tempROE) / float(sConfig.CALC_ROE_WEIGHT_SUM) / 100.0)
        print("예상 ROE : %.2f%%" % (expectedROE*100))
        expectedProfitRatio = float(sConfig.EXPECTED_PROFIT_RATIO / 100.0)
        print("기대수익률 : %f%%" % (expectedProfitRatio*100))
        overProfit = int(c_controlling_interest * expectedROE - expectedProfitRatio)
        print("초과 이익 : ", format(overProfit, ',d'))

        #---------------------------------------------------------------------
        #기업가치(지속) = 지배주주지분 + 초과이익 / 기대수익률
        #---------------------------------------------------------------------
        compValueConst = int(c_controlling_interest + overProfit / expectedProfitRatio)
        print("기업가치(지속) : ", format(compValueConst, ',d'))
        
        #---------------------------------------------------------------------
        #sRIM          = 기업가지(지속) / 주식수
        #매도가격
        sRIM = int(compValueConst / shareCnt)
        print("\nsRIM : ", format(sRIM, ',d'))
        
        #기업가치(w90) = 지배주주 지분 + 초과이익 * (0.9 / (1 + 기대수익율 - 0.9))
        #sRIM_w90     = 기업가치(w90) / 주식수
        #적정가격
        compValueW90 = int(c_controlling_interest + overProfit * (0.9 / (1 + expectedProfitRatio - 0.9)))
        sRIM_w90 = int(compValueW90 / shareCnt)
        print("sRIM_w90 : ", format(sRIM_w90, ',d'))
        
        #기업가치(w80) = 지배주주 지분 + 초과이익 * (0.8 / (1 + 기대수익율 - 0.8))
        #sRIM_w80     = 기업가치(w80) / 주식수
        #매수 가격
        compValueW90 = int(c_controlling_interest + overProfit * (0.8 / (1 + expectedProfitRatio - 0.8)))
        sRIM_w80 = int(compValueW90 / shareCnt)
        print("sRIM_w80 : ", format(sRIM_w80, ',d'))
        print(" ")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<")
        #---------------------------------------------------------------------        
        df = pd.DataFrame({
            "Year": z_list_years,
            "ROE": d_list_ROE,
            "PER": e_list_PER,
            "PBR": f_list_PBR,
            "EPS": g_list_EPS
        })
        print(df[::-1])
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<")
        # if len(currentValue) > 1 :
        #     print("current Price : %d"%int(currentValue))
        # print("sRIM    : %d"%sRIM)
        # print("sRIM w90: %d"%sRIM_w90)
        # print("sRIM w80: %d"%sRIM_w80)
        # print("-------------------------------------")

        # # update 날짜
        
        # updateDate = str(datetime.today())
        # print(updateDate)
        
        # # 종목명, 종목코드, 총 주싟, 자기 주식수 table 정리 및 저장
        # tempList = [self.sC.T_UPDATE_DATE, self.sC.T_COMPANY_NAME, self.sC.T_COMPANY_CODE, self.sC.T_SHARE_PRICE, self.sC.T_TOTAL_SHARE, self.sC.T_SELF_SHARE, self.sC.T_SRIM, self.sC.T_SRIM90, self.sC.T_SRIM80]
        # raw_snapshot_ = {'':[updateDate, compName, compCode, currentValue, totalShareCnt, companySelfShareCnt, str(sRIM), str(sRIM_w90), str(sRIM_w80)]}
        # _snapshot_ = pd.DataFrame(raw_snapshot_)
        # _snapshot_.index = tempList
        # _snapshot_.T.to_csv(str(self._csvPath_/(csvFileName + self.sC.FILE_DELIMETER_SNAPSHOT + csvFileNameExt)))
    
        # # ROE, BPS, 지배주주지분  table 정리 및 저장
        # raw_data_ = {self.sC.T_ROE:roeList,
        #              self.sC.T_BPS:bpsList,
        #              self.sC.T_SHARE_HOLDERS:shareHoldersList}
        # _data_ = pd.DataFrame(raw_data_)
        # _data_.index = yearList

        # _data_.T.to_csv(str(self._csvPath_/(csvFileName + self.sC.FILE_DELIMETER_DATA + csvFileNameExt)))

        #tempIndexStr = f'{"":>9}  {_data_.index[0]:>9}  {_data_.index[1]:>9}  {_data_.index[2]:>9}  {_data_.index[3]:>9}'
        #tempROEStr   = f'{self.sC.T_ROE:>9}  {_data_[self.sC.T_ROE][0]:>9}  {_data_[self.sC.T_ROE][1]:>9}  {_data_[self.sC.T_ROE][2]:>9}  {_data_[self.sC.T_ROE][3]:>9}'
        #tempBPSStr   = f'{self.sC.T_BPS:>9}  {_data_[self.sC.T_BPS][0]:>9}  {_data_[self.sC.T_BPS][1]:>9}  {_data_[self.sC.T_BPS][2]:>9}  {_data_[self.sC.T_BPS][3]:>9}'
        #tempSHSStr   = f'{self.sC.T_BPS:>9}  {_data_[self.sC.T_SHARE_HOLDERS][0]:>9}  {_data_[self.sC.T_SHARE_HOLDERS][1]:>9}  {_data_[self.sC.T_SHARE_HOLDERS][2]:>9}  {_data_[self.sC.T_SHARE_HOLDERS][3]:>9}'
        #print(tempIndexStr)
        #print(tempROEStr)
        #print(tempBPSStr)
        #print(tempSHSStr)


        # sRIM, sRIM_w90, sRIM_w80
        #_snapshot_['sRIM'] = str(sRIM)
        #_snapshot_['sRIM_w90'] = str(sRIM_w90)
        #_snapshot_['sRIM_w80'] = str(sRIM_w80)



#test = stockCrawlingDB()
#test.calculateAndSaveSRIMInfo(["../csv/KG_ETS_A151860_data_.csv","../csv/KG_ETS_A151860_snapshot_.csv"])
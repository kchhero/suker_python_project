import sys
from pandas import DataFrame

class stockCrawlingDB :
    compCode = ""
    
    def __init__(self) :
        pass
    
    def tableSetup(self, totalShareCnt, companySelfShareCnt, yearList, roeList, bpsList, shareHoldersList, compName, compCode):
        csvFileName = compName.replace(' ','_') + "_" + compCode + ".csv"
    
        # 종목명, 종목코드, 총 주싟, 자기 주식수 table 정리 및 저장
        raw_data1 = {'CompanyName':[compName],
                     'CompanyCode':[compCode],
                     'TotalShare':[totalShareCnt],
                     'SelfShare':[companySelfShareCnt],
                     ' ':[' ']}
        data1 = DataFrame(raw_data1)
        data1.align='r'
        data1.border=False
        data1.T.to_csv(csvFileName, header=False)
        
        # ROE, BPS, 지배주주지분  table 정리 및 저장
        raw_data2 = {'ROE':roeList, 'BPS':bpsList, 'shareHolders':shareHoldersList}
        data2 = DataFrame(raw_data2)
        data2.index = yearList
        data2.align='r'
        data2.border=False
        data2.T.to_csv(csvFileName, mode='a', header=True)

    def readAndShow(self, fileName) :
        pass
        
    def calculateAndSaveSRIMInfo(self) :
        pass
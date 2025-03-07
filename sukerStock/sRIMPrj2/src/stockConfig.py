# -*- coding: utf-8 -*-
import sys

class stockCrawlingCONFIG :
    DART_API_KEY = "e326eae7c94ec3be30fb9c8fb55f7749966555ae" # dart openapi key
    
    FAIL_UPDATE = 1
    FAIL_CALCULATE = 2
    FAIL_CSV_SAVE = 3
    FAIL_CSV_READ = 4
    FAIL_CSV_READ_NO_ONE_FILE = 5
    FAIL_CSV_READ_NO_ANY_FILE = 6

    T_UPDATE_DATE = "UpdateDate"
    T_COMPANY_NAME = "CompanyName"
    T_COMPANY_CODE = "CompanyCode"
    T_SHARE_PRICE = "1Day-ago_Value"
    T_TOTAL_SHARE = "TotalShare"
    T_SELF_SHARE = "SelfShare"
    T_SRIM = "sRIM"
    T_SRIM90 = "sRIM_w90"
    T_SRIM80 = "sRIM_w80"
                    
    T_ROE = "ROE"
    T_BPS = "BPS"
    T_SHARE_HOLDERS = "shareHolders"

    FILE_DELIMETER_SNAPSHOT = "_snapshot_"
    FILE_DELIMETER_DATA = "_data_"

    LATEST_YEAR = "2024"
    KOSPI_PATH_NAME = "./stocksDetail_KOSPI"
    KOSDAQ_PATH_NAME = "./stocksDetail_KOSDAQ"
    KOSPI_REFINED_PATH_NAME = "./stocksRefined_KOSPI"
    KOSDAQ_REFINED_PATH_NAME = "./stocksRefined_KOSDAQ"
    
    CALC_ROE_WEIGHT0 = 1
    CALC_ROE_WEIGHT1 = 2
    CALC_ROE_WEIGHT2 = 3
    CALC_ROE_WEIGHT_SUM = CALC_ROE_WEIGHT0 + CALC_ROE_WEIGHT1 + CALC_ROE_WEIGHT2

    EXPECTED_PROFIT_RATIO = 7.81 #BBB-

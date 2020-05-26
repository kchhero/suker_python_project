# -*- coding: utf-8 -*-
import sys

class stockCrawlingCONFIG :
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

    CALC_ROE_WEIGHT0 = 0.3
    CALC_ROE_WEIGHT1 = 0.7
    CALC_ROE_WEIGHT2 = 1.5
    CALC_ROE_WEIGHT3 = 3.0
    CALC_ROE_WEIGHT_SUM = CALC_ROE_WEIGHT0 + CALC_ROE_WEIGHT1 + CALC_ROE_WEIGHT2 + CALC_ROE_WEIGHT3

    EXPECTED_PROFIT_RATIO = 7.81 #BBB-

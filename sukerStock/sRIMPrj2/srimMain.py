# -*- coding: utf-8 -*-


from src.stocksDataUpdateTest import stockDataUpdateTEST as sDU_TEST
from src.stocksDataUpdate import stockDataUpdate as sDU
from src.stocksDataRefined import stockDataRefined as sDR
from src.stocksDataAnalysis import stockDataAnalysis as sDA
from src.stocksDataShow import stockDataShow as sDS
from datetime import datetime

def debugOn():
        import debugpy
        
        debugpy.listen(("localhost", 5678))  # 원하는 포트 사용 가능
        print("Debugger is waiting for connection...")

        # VS Code에서 디버깅 세션이 연결될 때까지 기다림
        debugpy.wait_for_client()

        print("Debugger is connected, execution continues...")
        
def main():
        today = datetime.today().strftime("%Y%m%d")
        stockDatabaseCls = sDU(today)
        stockDataRefined = sDR(today)
        stockDataAnalysys = sDA()
        stockDataShow = sDS()
        stockDatabaseCls_TEST = sDU_TEST(today)
        
        #debugOn()

        while True:
                print("")
                print("------------------------------------------------------------------------------------------------------")
                print("-------------------------------------- 주식 데이터 수집 프로그램 ---------------------------------------")
                print("1. KOSPI/KOSDAQ 모든 종목 한번에 내려받기 ==> ./stocksList/all_corp_raw.txt")
                print("2. KOSPI 모든 종목 table 업데이트 ==> ./stocksDetail_KOSPI/stockcode_code_tx_name_date.txt")
                print("3. KOSDAQ 모든 종목 table 업데이트 ==> ./stocksDetail_KOSDAQ/stockcode_code_tx_name_date.txt")
                print("4. 특정 종목 table 업데이트 ==> ./stocksDetail_KOSPI(KOSDAQ)//stockcode_code_tx_name_date.txt")
                print("5. KOSPI 모든 종목 ReFined(자사주, ROE, 주식수등 정리) ==> ./stocksDetail_KOSPI//stockcode_code_name_date.txt")
                print("6. KOSDAQ 모든 종목 ReFined(자사주, ROE, 주식수등 정리) ==> ./stocksDetail_KOSDAQ//stockcode_code_name_date.txt")
                print("7. 특정 종목 ReFined(자사주, ROE, 주식수등 정리) ==> ./stocksDetail_KOSPI(KOSDAQ)//stockcode_code_name_date.txt")
                print("8. KOSPI 모든 종목 sRIM 계산")
                print("9. KOSDAQ 모든 종목 sRIM 계산")
                print("10. 특정 종목 sRIM 계산")
                print("11. 특정 종목의 raw data show")
                print("22. TEST")
                print("0. 종료")
                print("------------------------------------------------------------------------------------------------------")
                menu = input("메뉴를 선택하세요: ")
                if menu == '1':
                        #Using Dart OpenAPI
                        stockDatabaseCls.searchAll()                    
                elif menu == '2':
                        stockDatabaseCls.searchTable_all('Y') #KOSPI
                elif menu == '3':
                        stockDatabaseCls.searchTable_all('K') #KOSDAQ
                elif menu == '4':
                        stock_code = input("종목코드를 입력하세요: ")
                        market_type = input("KOSPI면 Y, KOSDAQ이면 K를 입력하세요: ")
                        stockDatabaseCls.searchOneCompany(market_type, stock_code)
                elif menu == '5':                        
                        stockDataRefined.refineDataAll("Y")
                elif menu == '6':
                        stockDataRefined.refineDataAll("K")
                elif menu == '7':                    
                        stock_code = input("종목코드를 입력하세요: ")
                        market_type = input("KOSPI면 Y, KOSDAQ이면 K를 입력하세요: ")
                        stockDataRefined.oneRefine(market_type, stock_code)           
                elif menu == '8':
                        pass
                elif menu == '9':
                        pass
                elif menu == '10':
                        stock_code = input("종목코드를 입력하세요: ")
                        market_type = input("KOSPI면 Y, KOSDAQ이면 K를 입력하세요: ")        
                        stockDataAnalysys.sRIM(market_type, stock_code)
                elif menu == '11':
                        stock_code = input("종목코드를 입력하세요: ")
                        market_type = input("KOSPI면 Y, KOSDAQ이면 K를 입력하세요: ")        
                        stockDataShow.stock(market_type, stock_code)
                elif menu == '0':
                        print("프로그램을 종료합니다.")
                        break
                else:
                        print("잘못된 입력입니다. 다시 입력해주세요.")

    
if __name__ == "__main__":
    main()
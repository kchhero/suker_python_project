import dart_fss as dart # type: ignore
import pandas as pd # type: ignore
from urllib import parse
from .stockConfig import stockCrawlingCONFIG as sConfig
import time
import concurrent.futures
import queue
from pathlib import Path
import glob

class stockDataUpdate:
        eventQueue = queue.Queue()      # URL 큐 생성
        today = ""
        FETCH_WORKERS = 5
        FETCH_DELAY = 3 #seconds
        
        def __init__(self, today):
                self.today = today
        
        def searchAll(self) :
                dart.set_api_key(api_key=sConfig.DART_API_KEY)
                kosdaq_all = dart.api.market.get_stock_market_list('K', True)                
                kosdaq_df = pd.DataFrame.from_dict(kosdaq_all, orient='index').reset_index()
                kosdaq_df.columns = ['stock_code', 'sector', 'product', 'corp_cls', 'corp_name']
                kosdaq_df = kosdaq_df[['stock_code', 'corp_name', 'sector', 'product']]
                print("KOSDAQ ==> \n", kosdaq_df)
                
                kospi_all = dart.api.market.get_stock_market_list('Y', True)
                kospi_df = pd.DataFrame.from_dict(kospi_all, orient='index').reset_index()
                kospi_df.columns = ['stock_code', 'sector', 'product', 'corp_cls', 'corp_name']
                kospi_df = kospi_df[['stock_code', 'corp_name', 'sector', 'product']]
                print("KOSPI ==> \n", kospi_df)                
                
                kosdaq_df.to_csv("./stocksList/all_corp_kosdaq.txt", sep='\t', index=False)
                kospi_df.to_csv("./stocksList/all_corp_kospi.txt", sep='\t', index=False)

        def searchOneCompany(self, marketType, stock_code):
                url = self.generate_url_from_fnguide(stock_code)
                tables = self.get_tables_from_fnguide(url)
                #search corp_name from all_corp_kosdaq.txt or all_corp_kospi.txt
                if marketType == 'K' or marketType == "k":
                        rfile = open("./stocksList/all_corp_kosdaq.txt", "r", encoding='UTF8')
                elif marketType == 'Y' or marketType == "y":
                        rfile = open("./stocksList/all_corp_kospi.txt", "r", encoding='UTF8')
                else:
                        print("잘못 입력하셨습니다.")
                        return
                lines = rfile.readlines()
                rfile.close()
                
                corp_name = ""
                for line in lines:
                        line = line.strip()
                        line = line.split("\t")
                        if line[0] == stock_code:
                                corp_name = line[1]
                                break

                self.set_table11_to_txt(tables[11], stock_code, corp_name)
                self.set_table3_to_txt(tables[3], stock_code, corp_name)
                                
        def searchTable_all(self, marketType):
                rfile = ""
                if marketType == 'Y' or marketType == "y":
                        rfile = open("./stocksList/all_corp_kospi.txt", "r", encoding='UTF8')                        
                elif marketType == 'K' or marketType == "k":
                        rfile = open("./stocksList/all_corp_kosdaq.txt", "r", encoding='UTF8')
                else:
                        print("wrong parameter error")
                        return
                
                lines = rfile.readlines()                
                rfile.close()
                
                # 첫번째 line은 삭제
                print("this line remove ==> lines[0]: ", lines[0])
                lines = lines[1:]
                                
                corp_name = ""
                stock_code = ""
                        
                for line in lines:
                        line = line.strip()
                        line = line.split("\t")
                        # index0: stock_code, index:1 corp_name, index:2 corp_code
                        stock_code = line[0]
                        corp_name = line[1]                        
                        url = self.generate_url_from_fnguide(stock_code)
                        self.eventQueue.put([url, marketType, stock_code, corp_name])
                
                print("queue size : ", self.eventQueue.qsize())
                
                # 3개의 스레드 실행
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.FETCH_WORKERS) as executor:
                        futures = [executor.submit(self.fetch_url) for _ in range(self.FETCH_WORKERS)]

                # 모든 요청 완료 대기
                for future in concurrent.futures.as_completed(futures):
                        future.result()
                
                print("searchDetail_all() is done.")
                
        def fetch_url(self):
                while not self.eventQueue.empty():
                        infoArray = self.eventQueue.get()  # 큐에서 URL 가져오기
                        print("url : ", infoArray[0])
                        try:
                                tables = pd.read_html(infoArray[0], header=0)
                                if len(tables) < 3:
                                        print("fnguide 정보 이상 : ", infoArray[3])
                                else:
                                        self.set_table11_to_txt(tables[11], infoArray[1], infoArray[2], infoArray[3])
                                        self.set_table3_to_txt(tables[3], infoArray[1], infoArray[2], infoArray[3])
                                        print("save success : ", infoArray)                                        
                        except ValueError:
                                print("%s : fnguide 정보가 없음", infoArray[3])
                        except IndexError:
                                print("%s : fnguide 의 table 수 이상", infoArray[3])
                        finally:
                                self.eventQueue.task_done()  # 작업 완료 처리
                        time.sleep(self.FETCH_DELAY)
        
        def generate_url_from_fnguide(self, stock_code) :
                get_param = {
                        'pGB':1,
                        'gicode':'A%s'%(stock_code),
                        'cID':'',
                        'MenuYn':'Y',
                        'ReportGB':'',
                        'NewMenuID':101,
                        'stkGb':701,
                }
                get_param = parse.urlencode(get_param)
                url="http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?%s"%(get_param)
                return(url)
        
        def get_tables_from_fnguide(self, url) :                
                tables = pd.read_html(url, header=0)
                return(tables)

        def set_table11_to_txt(self, table, market_type, stock_code, corp_name) :
                if market_type == 'Y' or market_type == "y": #KOSPI
                        table.to_csv(sConfig.KOSPI_PATH_NAME + "/stockcode_%s_11_%s_%s.txt"%(stock_code, corp_name, self.today), sep='\t', index=False)
                elif market_type == 'K' or market_type == "k": #KOSDAQ
                        table.to_csv(sConfig.KOSDAQ_PATH_NAME + "/stockcode_%s_11_%s_%s.txt"%(stock_code, corp_name, self.today), sep='\t', index=False)
                else:
                        print("파일 저장중 잘못된 market type을 받았습니다.")
                
        def set_table3_to_txt(self, table, market_type, stock_code, corp_name) :
                if market_type == 'Y' or market_type == "y": #KOSPI
                        table.to_csv(sConfig.KOSPI_PATH_NAME + "/stockcode_%s_3_%s_%s.txt"%(stock_code, corp_name, self.today), sep='\t', index=False)
                elif market_type == 'K' or market_type == "k": #KOSDAQ
                        table.to_csv(sConfig.KOSDAQ_PATH_NAME + "/stockcode_%s_3_%s_%s.txt"%(stock_code, corp_name, self.today), sep='\t', index=False)
                else:
                        print("파일 저장중 잘못된 market type을 받았습니다.")

                       
        # def get_roe(self, code) :
        #         #annual = get_fnguide(code)[11] # annual financial highlight table
        #         print("=======================================")
        #         print(annual.iloc[18][3:6].tolist()) # 최근 3개년 확정 ROE


#def hotnews():        
                # 실적속보 page에 내 관심 종목과 일치하는 종목이 있는지 확인하여 print
                # 위 site page를 가져와야한다.
                # url="https://comp.fnguide.com/SVO2/ASP/SVD_ProResultCorp.asp?pGB=1&gicode=A102780&cID=&MenuYn=Y&ReportGB=&NewMenuID=503&stkGb=770"
                # tables = pd.read_html(url, header=0)
                # print(tables)[0]
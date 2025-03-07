import dart_fss as dart # type: ignore
import pandas as pd # type: ignore
from urllib import parse
from .stockConfig import stockCrawlingCONFIG as sConfig
import time
import concurrent.futures
import queue
from pathlib import Path
import glob

class stockDataRefined:
        today = ""
        def __init__(self, today):
                self.today = today
        
        def oneRefine(self, market_type, stock_code):
                folder_path = ""
                if market_type == 'K' or market_type == "k":
                        folder_path = Path(sConfig.KOSDAQ_PATH_NAME)
                elif market_type == 'Y' or market_type == "y":
                        folder_path = Path(sConfig.KOSPI_PATH_NAME)
                else:
                        print("folder_path setting fail")
                        return
                
                refined_data = {}
                refined_data["자사주"] = "0"
                                
                matching_files = list(folder_path.glob(f"stockcode_{stock_code}_*.txt"))
                if len(matching_files) >= 3:
                        print("Need to be files clean")
                        return
                elif len(matching_files) == 0:
                        print("file not found : ", stock_code)
                        return
                elif len(matching_files) == 2:
                        print("Good first step")
                else:
                        print("This step was occured error")
                        return
                    
                file_3_path = next(folder_path.glob(f"stockcode_{stock_code}_3_*.txt"), None)
                file_11_path = next(folder_path.glob(f"stockcode_{stock_code}_11_*.txt"), None)
                company_name = ""
                
                if file_3_path:
                        company_name = self.file_3_proc(file_3_path, refined_data)

                if file_11_path:
                        self.file_11_proc(file_11_path, refined_data)
                
                #write to file                
                file_w_name = "stockcode_" + stock_code + "_" + company_name + "_" + self.today + ".txt"
                self.writeRefineData(market_type, file_w_name, refined_data)                
        
        def refineDataAll(self, market_type):
                folder_path = ""
                if market_type == 'K' or market_type == "k":
                        folder_path = Path(sConfig.KOSDAQ_PATH_NAME)
                elif market_type == 'Y' or market_type == "y":
                        folder_path = Path(sConfig.KOSPI_PATH_NAME)
                else:
                        print("folder_path setting fail")
                        return                
                
                #KOSPI
                matching_files = list(folder_path.glob(f"stockcode_*_3_*.txt"))
                #get stock_code in filename
                stock_codeList = []
                for f in matching_files:
                        temp = f.name.split("_")
                        stock_codeList.append(temp[1])
                                
                stock_codeList = set(stock_codeList)

                for code in stock_codeList:
                        refined_data = {}
                        refined_data["자사주"] = "0"
                        company_name = ""
                        
                        file_3_path = next(folder_path.glob(f"stockcode_{code}_3_*.txt"), None)
                        file_11_path = next(folder_path.glob(f"stockcode_{code}_11_*.txt"), None)
                
                        if file_3_path:
                                company_name = self.file_3_proc(file_3_path, refined_data)

                        if file_11_path:
                                self.file_11_proc(file_11_path, refined_data)

                        #write to file
                        print("write to file")
                        file_w_name = "stockcode_" + code + "_" + company_name + "_" + self.today + ".txt"
                        self.writeRefineData(market_type, file_w_name, refined_data)
        
        def file_3_proc(self, file_3_path, refined_data):
                with file_3_path.open("r", encoding="utf-8") as f:
                        #get company name                                
                        company_name_temp = file_3_path.name.split("_")     
                        for line in f:#content:
                                #compare encoding string
                                if "자사주" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["자사주"] = line[1]
                                        print("find out 자사주 : ", line[1])
                                        break
                                else:
                                        refined_data["자사주"] = "0"
                                        print("자사주 not found")
                        return company_name_temp[3]

        def file_11_proc(self, file_11_path, refined_data):
                with file_11_path.open("r", encoding="utf-8") as f:
                        for line in f:
                                if "IFRS(연결)" in line:
                                        if "Annual" not in line:
                                                line = line.strip()
                                                line = line.split("\t")
                                                refined_data["Years"] = line[1:]
                                                print("find out Years : ", line[1:])
                                elif "ROE" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["ROE"] = line[1:]
                                        print("find out ROE : ", line[1:])
                                elif "PER" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["PER"] = line[1:]
                                        print("find out PER : ", line[1:])
                                elif "PBR" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["PBR"] = line[1:]
                                        print("find out PBR : ", line[1:])
                                elif "발행주식수" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["TOTAL_STOCKS"] = line[1:]
                                        print("find out 발행주식수 : ", line[1:])
                                elif "EPS" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        refined_data["EPS"] = line[1:]
                                        print("find out EPS : ", line[1:])
                                elif "지배주주지분" in line:
                                        line = line.strip()
                                        line = line.split("\t")
                                        if line[0] == "지배주주지분":                                                
                                                refined_data["ContollingInt"] = line[1:]
                                                print("find out 지배주주지분 : ", line[1:])
                
        def writeRefineData(self, market_type, filename, data):
                folder_path = ""
                if market_type == 'K' or market_type == "k":
                        folder_path = Path(sConfig.KOSDAQ_REFINED_PATH_NAME)
                elif market_type == 'Y' or market_type == "y":
                        folder_path = Path(sConfig.KOSPI_REFINED_PATH_NAME)
                else:
                        print("folder_path setting fail")
                        return
                with folder_path.joinpath(filename).open("w+", encoding="utf-8") as f:
                        try:
                                f.write("IFRS(연결)\t%s\n"%data["Years"])
                                f.write("자사주\t%s\n"%data["자사주"])
                                f.write("발행주식수\t%s\n"%data["TOTAL_STOCKS"])
                                f.write("ROE\t%s\n"%data["ROE"])
                                f.write("PER\t%s\n"%data["PER"])
                                f.write("PBR\t%s\n"%data["PBR"])
                                f.write("EPS\t%s\n"%data["EPS"])
                                f.write("지배주주지분\t%s\n"%data["ContollingInt"])
                        except KeyError:
                                print("Error file is ", filename)                                
                        finally:
                                print("write to file : ", filename)
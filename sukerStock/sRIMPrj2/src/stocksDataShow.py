# -*- coding: utf-8 -*-
from pathlib import Path
from .stockConfig import stockCrawlingCONFIG as sConfig
import ast
import pandas as pd # type: ignore
from itertools import zip_longest

class stockDataShow :
    def __init__(self) :
        pass
    
    def stock(self, marketType, stockCode):
        folderPath = ""
        
        if marketType == "Y" or marketType == "y":
            folderPath = Path(sConfig.KOSPI_PATH_NAME)
        elif marketType == "K" or marketType == "k":
            folderPath = Path(sConfig.KOSDAQ_PATH_NAME)
        else:
            print("Market Type is Strange")
            exit()

        filePath = next(folderPath.glob(f"stockcode_{stockCode}_11_*.txt"), None)
        
        company_name = filePath.name.split("_")[3]

        alist = []
        blist = []
        clist = []
        dlist = []
        elist = []
        flist = []
        glist = []
        hlist = []
        ilist = []
        jlist = []
        klist = []
        llist = []
        mlist = []
        nlist = []
        olist = []
        plist = []
        qlist = []
        rlist = []
        slist = []
        
        with filePath.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if "IFRS(연결)" in line:
                    if "Annual" not in line:
                        conlist = line[1:]
                        alist = conlist[:]
                elif "매출액" in line:
                    conlist = line[1:]
                    blist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "영업이익" in line:
                    conlist = line[1:]
                    clist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "당기순이익" in line:
                    conlist = line[1:]
                    dlist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "지배주주순이익" in line:
                    conlist = line[1:]
                    elist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "자산총계" in line:
                    conlist = line[1:]
                    flist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "부채총계" in line:
                    conlist = line[1:]
                    glist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "자본총계" in line:
                    conlist = line[1:]
                    hlist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "지배주주지분" in line:
                    conlist = line[1:]
                    ilist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "자본금" in line:
                    conlist = line[1:]
                    jlist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "유보율" in line:
                    conlist = line[1:]
                    klist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "영업이익률" in line:
                    conlist = line[1:]
                    llist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "지배주주순이익률" in line:
                    conlist = line[1:]
                    mlist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "ROA" in line:
                    conlist = line[1:]
                    nlist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "ROE" in line:                    
                    conlist = line[1:]
                    olist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "EPS(원)" in line:
                    conlist = line[1:]
                    plist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]]
                elif "BPS(원)" in line:
                    conlist = line[1:]
                    qlist = [int(x) if x not in ("", "N/A(IFRS)") else 0 for x in conlist[:]] 
                elif "PER" in line:
                    conlist = line[1:]
                    rlist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 
                elif "PBR" in line:
                    conlist = line[1:]
                    slist = [float(x) if x not in ("", "N/A(IFRS)") else 0.0 for x in conlist[:]] 


        # 가장 긴 리스트에 맞춰 다른 리스트를 NaN으로 채우기
        data = list(zip_longest(alist, blist, clist, dlist,elist,flist,glist,hlist,ilist,jlist,klist,llist,mlist,nlist,olist,plist,qlist,rlist,slist,
                                 fillvalue=None))
        # DataFrame 생성
        df = pd.DataFrame(data, columns=["IFRS(연결)", "매출액", "영업이익", "당기순이익", "지배주주순이익", "자산총계", 
                                        "부채총계", "자본총계", "지배주주지분", "자본금", "유보율", "영업이익률", "지배주주순이익률", 
                                        "ROA", "ROE", "EPS(원)", "BPS(원)", "PER", "PBR"])
        print(">>>>>>><<<<<<<")
        print(" %s"%company_name)     
        print(">>>>>>><<<<<<<")
        df["IFRS(연결)"] = df["IFRS(연결)"].apply(lambda x: f"{x:<10}")  # 왼쪽 정렬 (:<200)
        print(df.T)
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<")
        
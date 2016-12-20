#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
import sys

mainLottoUrl = "https://www.nlotto.co.kr/lotto645Confirm.do?method=byWin"
latestLottoUrl = "https://www.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo="
DEBUG=False

lottoPosts = []
lottoPostsTest = [{"timeid" : "999992", "numbers" : "2,4,5,17,27,32+43", "num1count" : "7", "amount": "2,203,270,608"},
                  {"timeid" : "999991", "numbers" : "23,41,5,4,7,32+43", "num1count" : "5", "amount": "1,203,270,608"}
                 ]
lotto_mdb_name = 'lottodb'
lotto_mdb_name_test = 'lottodbTest'

class lottoWithMongoDB:
    dbClient = ''
    dbHandle = ''
    dbCollection = ''
    lotto_list = []
    
    def connectMDBC(self):
        self.dbClient = MongoClient('mongodb://localhost')
        self.dbHandle = self.dbClient[lotto_mdb_name]
        self.dbCollection = self.dbHandle.lottoCollectionTest

        if DEBUG==True:
            self.clearMDB("732")
            self.clearMDB("999992")
            self.clearMDB("999991")
            post_id = self.dbCollection.insert(lottoPostsTest)
            print post_id
            print self.dbHandle.collection_names()
            print self.dbCollection.find_one({"timeid":"999992"})   # if author==Mike ==> print post
            print self.dbCollection.find_one({"timeid":"999991"})   # if author==Mike ==> print post

            
    def clearMDB(self, id):
        self.dbCollection.remove({"timeid":id})
        self.dbCollection.remove({"author":"Mike"})
        
    def checkLatestNumber(self):
        resp = requests.get(mainLottoUrl)
        soup = BeautifulSoup(resp.text, "lxml")
        line = str(soup.find("meta", {"id" : "desc", "name" : "description"})['content'])

        print line

        begin = line.find(" ")
        end = line.find("회")

        if begin == -1 or end == -1:
            print("not found last lotto number")
            exit()

        return int(line[begin+1:end])


    def checkLatestNumberInMDB(self, id):
        if self.dbCollection.find_one({"timeid":id}) != None :
            print "Already latest lotto numbers saved"
        else:
            #find last saved number
            #ASCENDING
            cursor = self.dbCollection.find().sort("timeid",pymongo.DESCENDING).limit(1)
            for document in cursor :                
                return document["timeid"]


    def crawler(self, start, end):
        for i in range(start, end + 1):
            crawler_url = latestLottoUrl + str(i)
            print("crawler: " + crawler_url)

            resp = requests.get(crawler_url)
            soup = BeautifulSoup(resp.text, "lxml")
            line = str(soup.find("meta", {"id": "desc", "name": "description"})['content'])

            begin = line.find("당첨번호")
            begin = line.find(" ", begin) + 1
            end = line.find(".", begin)
            numbers = line[begin:end]

            begin = line.find("총")
            begin = line.find(" ", begin) + 1
            end = line.find("명", begin)
            persons = line[begin:end]

            begin = line.find("당첨금액")
            begin = line.find(" ", begin) + 1
            end = line.find("원", begin)
            amount = line[begin:end]

            info = {}
            info["timeid"] = i
            
            #numbers
            temp = []
            realnumbers = ''
            temp = numbers.split(',')
 
            lastnum = temp[-1].split('+')[0]
            bonus = temp[-1].split('+')[1]
            temp[-1] = lastnum
    
            for i in temp:
                realnumbers += i+' '

            info["numbers"] = realnumbers.strip(' ')
            info["bonusnum"] = bonus
            info["num1count"] = persons
            info["amount"] = amount
            
            self.lotto_list.append(info)            

    def insert(self):
        post_id = self.dbCollection.insert(self.lotto_list)

    def showdb(self):
        cursor = self.dbCollection.find().sort("timeid",pymongo.DESCENDING)
        for document in cursor :
            print document

    def removedbAll(self):
        self.dbCollection.remove()
        
    def findnumbers(self,ff):
        cursor = self.dbCollection.find_one({"numbers":ff})
        if cursor == None:
            print "당첨 번호 없음"
        else :
            print "회    차 : " + str(cursor[("timeid")]) + "회"
            print "당첨번호 : " + cursor[("numbers")]
            print "1등 금액 : " + cursor[("amount")] + "원"        
    def findtime(self, tt):    
        cursor = self.dbCollection.find_one({"timeid":int(tt)})
        if cursor == None:
            print "해당 최차 정보 없음"
        else :
            print "회    차 : " + str(cursor[("timeid")]) + "회"
            print "당첨번호 : " + cursor[("numbers")]
            print "1등 금액 : " + cursor[("amount")] + "원"
            
def main(arg1):
    mdbLottoinst = lottoWithMongoDB()
    mdbLottoinst.connectMDBC()
    
    if arg1=="cleardb" :
        mdbLottoinst.removedbAll()
    elif arg1=="showdb" :
        mdbLottoinst.showdb()
    elif arg1=="updatedb" :
        latestNum = mdbLottoinst.checkLatestNumber()
        dbNum = mdbLottoinst.checkLatestNumberInMDB(str(latestNum))

        if dbNum == None:
            print "db is empty"
            mdbLottoinst.crawler(1, latestNum)
            mdbLottoinst.insert()
        elif dbNum < latestNum:
            print("latest time " + str(latestNum) + ", database have " + str(dbNum) + " time saved.")
            print("now update start...")
            mdbLottoinst.crawler(dbNum+1, latestNum)
            mdbLottoinst.insert()
        else:
            print "Already DB is latest updated"
            mdbLottoinst.showdb()
    elif arg1=="findnum":
        numbers = raw_input()
        mdbLottoinst.findnumbers(numbers)
    elif arg1=="findtime":
        numbers = raw_input()
        mdbLottoinst.findtime(numbers)
    else:
        print "------ Usage check below -------"
        print "python sukerLotto_mdb.py showdb"
        print "python sukerLotto_mdb.py cleardb"
        print "python sukerLotto_mdb.py updatedb"
        print "python sukerLotto_mdb.py findnum"
        print "python sukerLotto_mdb.py findtime"
        print "--------------------------------"
        
if __name__ == "__main__":
    main(sys.argv[1])

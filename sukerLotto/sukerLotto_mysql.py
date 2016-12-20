#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup
import MySQLdb
import sys

#mysql
#   $ mysql -u root -p
#   mysql> create user 'lotto'@'localhost' identified by 'pwlotto';
#   mysql> grant all privileges on *.* to 'lotto'@'localhost';
#   mysql> grant all privileges on lottodb.* to 'lotto'@'localhost';
#
#   delete ==>   mysql> DROP USER [username]@[servername];
#   check  ==>   mysql> show grants for lotto@localhost;
#
#   DB check ==> mysql> show databases;
#                mysql> create database DBname;

lotto_list = []

SQL_ARGS_HOST="localhost"
SQL_ARGS_USER="lotto"
SQL_ARGS_PW="pwlotto"
SQL_ARGS_DBNAME="lottodb"

main_url = "https://www.nlotto.co.kr/lotto645Confirm.do?method=byWin"
# every week
basic_url = "https://www.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo="

def getLast():
    resp = requests.get(main_url)
    soup = BeautifulSoup(resp.text, "lxml")
    line = str(soup.find("meta", {"id" : "desc", "name" : "description"})['content'])

    print line
    
    begin = line.find(" ")
    end = line.find("회")

    if begin == -1 or end == -1:
        print("not found last lotto number")
        exit()

    return int(line[begin + 1 : end])


def checkLast():
    db = MySQLdb.connect(host=SQL_ARGS_HOST, user=SQL_ARGS_USER, passwd=SQL_ARGS_PW, db=SQL_ARGS_DBNAME)
    cursor = db.cursor()
    sql = "SELECT MAX(count) FROM data"

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result[0]
    except:
        print(sys.exc_info()[0])

    cursor.close()
    db.close()

    return 0

def crawler(fromPos, toPos):
    #for i in range(fromPos + 1, toPos + 1):
    for i in range(1, 10):
        crawler_url = basic_url + str(i)
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
        info["회차"] = i
        info["번호"] = numbers
        info["당첨자"] = persons
        info["금액"] = amount

        lotto_list.append(info)            

def insert():
        db = MySQLdb.connect(host=SQL_ARGS_HOST, user=SQL_ARGS_USER, passwd=SQL_ARGS_PW, db=SQL_ARGS_DBNAME)
        cursor = db.cursor()

        for dic in lotto_list:
            count = dic["회차"]
            numbers = dic["번호"]
            persons = dic["당첨자"]
            amounts = dic["금액"]

            print("insert to database at " + str(count))

            numberlist = str(numbers).split(",")

            sql = "INSERT INTO `lotto`. `data`(`count`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `persion`, `amount`) " \
                  "VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s')" \
                  % (count,
                     int(numberlist[0]),
                     int(numberlist[1]),
                     int(numberlist[2]),
                     int(numberlist[3]),
                     int(numberlist[4]),
                     int(numberlist[5].split("+")[0]),
                     int(numberlist[5].split("+")[1]),
                     int(persons),
                     str(amounts))

            try:
                cursor.execute(sql)
                db.commit()
            except:
                print(sys.exc_info()[0])
                db.rollback()
                break

        cursor.close()
        db.close()
            
def main():
    last = getLast()
    dblast = checkLast()

    if dblast < last:
        print("latest time " + str(last) + ", database have " + str(dblast) + " time saved.")
        print("now update start...")
        crawler(dblast, last)

    insert()

if __name__ == "__main__":
    main()

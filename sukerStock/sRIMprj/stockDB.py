import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import MySQLdb

SQL_ARGS_HOST="localhost"
SQL_ARGS_USER="suker"
SQL_ARGS_PW="suker"
SQL_ARGS_DBNAME="sukerDB"

main_url = ""
basic_url = ""

# def getLast():
#     resp = requests.get(main_url)
#     soup = BeautifulSoup(resp.text, "lxml")
#     line = str(soup.find("meta", {"id" : "desc", "name" : "description"})['content'])

#     print line
    
#     begin = line.find(" ")
#     end = line.find("회")

#     if begin == -1 or end == -1:
#         print("not found last lotto number")
#         exit()

#     return int(line[begin + 1 : end])


def searchCode():
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
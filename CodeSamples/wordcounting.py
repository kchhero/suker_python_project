defg = []
myword = {}


def readTxtFile() :
    with open("temp.txt") as f :
        abc = f.readlines()
        for i in abc :
            defg = i.split(" ")
            for j in defg :
                if myword.get(j) is None :
                    myword[j] = 1
                else :
                    temp = myword[j]
                    temp += 1
                    myword[j] = temp

    print(myword)

readTxtFile()

import sys
import os

def scrapping(startPath, destPath) :
    for dir in os.listdir(startPath) :
        userPath = startPath + '/' + dir
        userBashHistory = userPath + '/' + '.bash_history'
        if os.path.exists(userBashHistory) :
            os.system("cp "+userBashHistory+ " " +destPath)

def main(path,path2) :
    scrapping(path,path2)

if __name__ == "__main__":
    try :
        main(sys.argv[1],sys.argv[2])
    finally :
        pass


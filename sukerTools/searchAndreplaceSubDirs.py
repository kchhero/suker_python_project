# Usage : python searchAndreplaceSubDirs.py <path> srcStr destStr <depth> <ext>
# Full path and .py files recursive replace :
#      python searchAndreplaceSubDirs.py . abc def all .py
#      python searchAndreplaceSubDirs.py . abc def all "*"
# Current dir and .sh files recursive replace :
#      python searchAndreplaceSubDirs.py . abc def current .sh
#      python searchAndreplaceSubDirs.py . abc def current "*"

import os
import sys
import fileinput


fileList = []


def currentOnly(dirname, extension):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if extension != "*" :
                if extension == os.path.splitext(full_filename)[-1] :
                    fileList.append(os.path.abspath(full_filename))
                    # print(os.path.abspath(full_filename))
            else :
                fileList.append(os.path.abspath(full_filename))
                # print(os.path.abspath(full_filename))

    except PermissionError:
        pass


def fullPathDoing(dirname, extension) :
    try:
        for (path, dir, files) in os.walk(dirname):
            for filename in files:
                if extension != '*' :
                    if extension == os.path.splitext(filename)[-1] :
                        fileList.append("%s/%s" % (os.path.abspath(path), filename))
                        # print("%s/%s" % (os.path.abspath(path), filename))
                else :
                    fileList.append("%s/%s" % (os.path.abspath(path), filename))
                    # print("%s/%s" % (os.path.abspath(path), filename))
    except PermissionError:
        pass


def doReplace(srcStr, destStr) :
    for i in fileList :
        print (i)
        print ("\n")
        for line in fileinput.input(i, inplace = 1):
            print(line.replace(srcStr, destStr)),


def usage() :
    print("===============================================================================")
    print(" Usage : python searchAndreplaceSubDirs.py <path> srcStr destStr <depth> <ext>")
    print(" Full path and .py files recursive replace :")
    print("      python searchAndreplaceSubDirs.py . abc def all .py")
    print("      python searchAndreplaceSubDirs.py . abc def all '*'")
    print(" Current dir and .sh files recursive replace :")
    print("      python searchAndreplaceSubDirs.py . abc def current .sh")
    print("      python searchAndreplaceSubDirs.py . abc def current '*'")
    print("===============================================================================")
    print("")
    print("Try Again !")
    print("")


def main(path, srcStr, destStr, depth, extension):
    if extension == '*' :
        print ("Full ext")

    if depth == 'all' :
        fullPathDoing(path, extension)
    else :
        currentOnly(path, extension)

    # print (fileList)
    doReplace(srcStr, destStr)


if __name__ == "__main__":
    try :
        # print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    except IndexError :
        usage()

    finally :
        pass

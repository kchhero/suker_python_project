# -*- coding: utf-8 -*-

import zipfile
import os

class extractfile():
    def __init__(self, *args, **kwds):
        pass
    
    def gogo(self):
        self.extractZipFileForHasPwd("asdf.zip", "qawert")
            
    def extractZipFileForNoPwd(self, filename=None):
        if filename is None :
            return
        else:
            zFile = zipfile.ZipFile(filename)
            zFile.extractall(pwd=None,path=os.getcwd()+"/"+filename)

    def extractZipFileForHasPwd(self, filename="", pwd=""):
        if filename is "":
            return
        elif pwd is "":
            print "You need input the password"
            return
        else:
            zFile = zipfile.ZipFile(filename)
            try:
                zFile.extractall(pwd=pwd,path=os.getcwd()+"/"+filename.split('.')[0])
            except Exception,e:
                print e
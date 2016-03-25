# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:31:41 2014

@author: choonghyun.jeon
"""

import subprocess
import shutil
import os

commands={'NAME_ONLY':['git','status','-s'],
          'TOPLEVEL_PATH':['git','rev-parse','--show-toplevel']}
NEW_DIR_NAME = '___diff_new_dir___'

class gitDiffToFiles :
    def __init__(self, workingSpace, promptColors) :
        self.fileList = []
        self.dirList = []
        self.workingSpace = workingSpace
        self.newDirName = NEW_DIR_NAME+'/'+workingSpace+'/'
        self.isExistNewDir = False
        self.prompt = promptColors
    
    def printLine(self, _type_) :
        if _type_==1 :
            return "------------------------------------------------------------------"
        elif _type_==2 :
            return "----------"
            
    def commandGit(self) :
        if os.path.exists(".git")==False :
            print self.prompt["RED"]+"Here is not exist '.git'"+self.prompt["ENDC"]
            return False
            
        try :
            out_bytes = subprocess.check_output(commands['NAME_ONLY'])
            tempL = list(out_bytes.split('\n'))
            
            if len(tempL)<=1 :
                print self.printLine(2) + self.prompt["YELLOW"]+"There is no diff file "+self.prompt["ENDC"] + self.printLine(2)
                print self.printLine(2) + " Please check the 'git diff' command " + self.printLine(2)
                print self.printLine(1) + "\n"
                return False
            else :                
                self.fileList = tempL[:]
                self.dirList = tempL[:]
                
                for i in tempL :
                    if len(i) <= 1 :
                        pass
                    else :
                        kk = (i.lstrip(' ')).split(' ')
                        temp = kk[1]
                        if temp[-1]=='/' : #directory
                            self.fileList.remove(i)
                        else :
                            self.dirList.remove(i)
                            
                print self.printLine(2)+self.prompt["YELLOW"]+"git diff file list"+self.prompt["ENDC"]+self.printLine(2)
                for i in self.dirList :
                    if len(i)<=1 :
                        self.dirList.remove(i)
                    else:
                        print "\t"+self.prompt["LIGHT_CYAN"]+i+self.prompt["ENDC"]
                for i in self.fileList :
                    if len(i)<=1 :
                        self.fileList.remove(i)
                    else:
                        print "\t"+self.prompt["LIGHT_CYAN"]+i+self.prompt["ENDC"]
                print self.printLine(1) + "\n"
                return True
                
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            print out_bytes, code

    def checkNewDir(self) :
        root_path = ""
        try :
            out_bytes = subprocess.check_output(commands['TOPLEVEL_PATH'])
            temp = out_bytes.split(self.workingSpace)
         
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            print out_bytes, code
        
        root_pathL = out_bytes.split(self.workingSpace)
        root_path = root_pathL[0]

        if len(temp)==1 :
            self.newDirName = root_path.rstrip()+'/'+self.newDirName.rstrip()
        else :
            self.newDirName = root_path+self.newDirName+root_pathL[1].lstrip('/').rstrip()+'/'      
        
        if os.path.exists(self.newDirName) :
            print "Already Exist " + self.newDirName + " directories..."            
        else :           
            os.makedirs(self.newDirName)
        self.isExistNewDir = True
    
    def createDir(self, path, _curDir) :
        if os.path.exists(self.newDirName + path)==False and len(path)!=0 :
            os.chdir(self.newDirName)
            os.makedirs(path)
            os.chdir(_curDir)
            print './' + self.newDirName + path + " dir create complete...  "
    
    def paseGitDiff(self) :
        _curDir = os.getcwd()
        if self.isExistNewDir==False :
            self.checkNewDir()
            
        for i in self.fileList :
            kk = (i.lstrip(' ')).split(' ')
            if kk[0]=='D' :
                print "----> " + self.prompt["LIGHT_RED"]+kk[1] + self.prompt["ENDC"] +\
                " is "+self.prompt["LIGHT_RED"]+"deleted file"+self.prompt["ENDC"]+", so does not copy\n"
            else :
                fname = os.path.basename(kk[1])
                dname = os.path.dirname(kk[1])
                self.createDir(dname, _curDir)                        
                shutil.copy(kk[1], self.newDirName + dname)
                print "----> copy file '" + self.prompt["LIGHT_GREEN"] + fname + self.prompt["ENDC"] + "' success!!\n"

        for i in self.dirList :
            kk = (i.lstrip(' ')).split(' ')
            if kk[0]=='D' :
                print "----> " + self.prompt["LIGHT_RED"]+kk[1] + self.prompt["ENDC"] +\
                " is "+self.prompt["LIGHT_RED"]+"deleted dir"+self.prompt["ENDC"]+", so does not copy\n"
            else :                
                dname = kk[1]                
                self.createDir(dname, _curDir)                        
                os.system("cp -a " + dname + " " + self.newDirName + dname+"../")
                print "----> copy dir '" + self.prompt["LIGHT_GREEN"] + dname + self.prompt["ENDC"] + "' success!!\n"
                
        print "Done!!!"
        print "Please Check path for : " + self.prompt["BOLD"]+self.prompt["LIGHT_YELLOW"] + self.newDirName + self.prompt["ENDC"] + "\n\n"
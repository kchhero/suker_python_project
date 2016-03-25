# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:19:47 2014

@author: choonghyun.jeon
"""

import sys
import os
import subprocess
import glob

_prompt_ = " >>> "
commandDict = {'q':'QUIT', 'quit':'QUIT', 'exit':'QUIT', 'b':'BACK', 'back':'BACK', 'h':'HELP', 'help':'HELP',
                   'sc':'SHOW_COMMAND_LIST', 'show':'SHOW_COMMAND_LIST'}
_extExceptFileNames = {'py':'__init__.py','sh':''}
_extFileNames = ['py','sh']
selectedWorkingSpace = None

fileListFromEachDirs = [[]] 

linuxMark = '/'
winMark = '\\'
    
promptColors={"BOLD":"\033[1m",
              "BACKGROUND":"\033[7m",
              "YELLOW":"\033[33m",
              "LIGHT_YELLOW":"\033[1;33m",
              "GREEN":"\033[32m",
              "LIGHT_GREEN":"\033[1;32m",
              "RED":"\033[31m",
              "LIGHT_RED":"\033[1;31m",
              "CYAN":"\033[36m",
              "LIGHT_CYAN":"\033[1;36m",
              "RED_BLINK":"\033[5;31m",
              "ENDC":"\033[0m"}

_DebugMarkStr_ = "suker Debug ==> "
_InfoMarkStr_ = " ** ==> "

class sukerScript :    
    def __init__(self, path1, path2) :
        self.thisScriptPath = path1
        self.workingPath = path2
        
    def printMenuLevel1(self) :
        print promptColors["YELLOW"]+_InfoMarkStr_+" script Path "+promptColors["ENDC"] +promptColors["LIGHT_CYAN"]+self.thisScriptPath+promptColors["ENDC"]
        print promptColors["YELLOW"]+_InfoMarkStr_+" working Path "+promptColors["ENDC"] +promptColors["LIGHT_CYAN"]+self.workingPath+promptColors["ENDC"]
        print "==========================================================="
        print promptColors["CYAN"]+"Choice script : "+promptColors["ENDC"] + promptColors["LIGHT_RED"]+"LEVEL 1"+promptColors["ENDC"]
        print "==========================================================="
        print 'select : '
        for i in fileListFromEachDirs :
            print "    "+promptColors["GREEN"] + "'"+i[0][0:2]+"'" + ' or ' + "'" + i[0] + "'" + promptColors["ENDC"]+" --> search scripts can show or run"    
        print "\n    "+promptColors["GREEN"]+"'q' or 'exit' or 'quit' "+promptColors["ENDC"]+" --> Quit this program"
        print "===========================================================\n"
        
    def printMenuLevel2(self, index) :
        print promptColors["YELLOW"]+_InfoMarkStr_+" working Path "+promptColors["ENDC"] +promptColors["LIGHT_CYAN"]+self.workingPath+promptColors["ENDC"]
        print "==========================================================="
        print promptColors["CYAN"]+"Choicet want script "+promptColors["ENDC"] + promptColors["LIGHT_RED"]+"LEVEL 2"+promptColors["ENDC"]
        print "==========================================================="
        print 'select : '
        cnt = 0
        for i in fileListFromEachDirs[index][1] :
            print "    "+promptColors["LIGHT_RED"] + str(cnt) + ' : ' + i + promptColors["ENDC"]+" --> select number..."
            cnt += 1
        print "    "+promptColors["GREEN"]+"'b'"+promptColors["ENDC"]+" --> back menu"
        print "    "+promptColors["GREEN"]+"'q' or 'exit' or 'quit'"+promptColors["ENDC"]+" --> Quit this program"
        print "===========================================================\n"
    
    def printScrpitsList(self) :
        print "==========================================================="
        print "==========================================================="
        print "select : "+promptColors["GREEN"]+"'sc' or 'show'"+promptColors["ENDC"]+" --> show git scripts lists"
        print "         "+promptColors["GREEN"]+"'b'"+promptColors["ENDC"]+" --> back menu"
        print "         "+promptColors["GREEN"]+"'q' or 'exit' or 'quit'"+promptColors["ENDC"]+" --> Quit this program"
        print "===========================================================\n"

    #def printUsage() :
    #    print "==========================================================="
    #    print promptColors["LIGHT_YELLOW"]+"Select want command"+promptColors["ENDC"]+"..."
    #    print "==========================================================="
    #    print "Command : "+promptColors["GREEN"]+"'a'"+promptColors["ENDC"]+" --> Create dir trees about diff files"
        #print "          "+promptColors["GREEN"]+"'b'"+promptColors["ENDC"]+" --> tbd"
    #    print "          "+promptColors["GREEN"]+"'h'"+promptColors["ENDC"]+" or 'help' --> show again Usage"
    #    print "          "+promptColors["GREEN"]+"'q'"+promptColors["ENDC"]+" or 'exit' or 'quit' --> Quit this program"
    #    print "===========================================================\n"
        
    def conversationLevel1(self) :
        wSpace = None
    
        while 1 :
            self.printMenuLevel1()
            wSpace = raw_input(_prompt_).lower()
            if wSpace in commandDict.keys() :
                if commandDict[wSpace]=='QUIT' :
                    print "GoodBye!! \n"
                    sys.exit()
                elif commandDict[wSpace]=='HELP' :
                    print "Fuck You! \n"
                else :
                    print "Fuck You! \n"
            else :
                tempCheckList = []
                tempCheckPreFixList = []
                for i in fileListFromEachDirs :
                    tempCheckList.append(i[0])
                    tempCheckPreFixList.append(i[0][0:2])
                    
                if wSpace in tempCheckList :
                    self.conversationLevel2(tempCheckList.index(wSpace))
                    break
                elif wSpace in tempCheckPreFixList :
                    self.conversationLevel2(tempCheckPreFixList.index(wSpace))
                    break
                else:
                    print "Fuck You! \n"
    
    def conversationLevel2(self, index) :
        self.printMenuLevel2(index)
        wSpace = None
    
        wSpace = raw_input(_prompt_).lower()
        if wSpace in commandDict.keys() :
            if commandDict[wSpace]=='QUIT' :
                print "GoodBye!! \n"
                sys.exit()
            elif commandDict[wSpace]=='BACK' :
                self.conversationLevel1()
        else :
            try :
                if int(wSpace) < 0 or int(wSpace) >= len(fileListFromEachDirs[index][1]):
                    print "Fuck You! \n"
                else :
                    self.runningScript(index, int(wSpace))
		    print "\n\n"
                    self.conversationLevel1()
            except ValueError :
                 print "Fuck You! \n"
            
    
    def runningScript(self, dirIndex, runIndex) :
        scriptName = self.thisScriptPath + linuxMark + fileListFromEachDirs[dirIndex][0] + linuxMark + fileListFromEachDirs[dirIndex][1][runIndex]
        #print _DebugMarkStr_+" scriptName ==>" + scriptName
        extName = os.path.splitext(scriptName)[1]
        excuteCommand = ''
        if extName=='.py' :
            excuteCommand = 'python'
        elif extName=='.sh' :
            excuteCommand = 'bash'
        else :
            pass
    
        #print _DebugMarkStr_+" before "+os.getcwd()
        os.chdir(self.workingPath)
        #print _DebugMarkStr_+" after "+os.getcwd()
        try :
            out_bytes = subprocess.check_call([excuteCommand,scriptName])
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            print out_bytes, code
        
        #print _DebugMarkStr_+" before "+os.getcwd()
        os.chdir(self.thisScriptPath)
        #print _DebugMarkStr_+" after "+os.getcwd()
        
    def scriptListGathering(self) :        
        #print promptColors["YELLOW"]+_InfoMarkStr_+" script Path "+promptColors["ENDC"] +promptColors["LIGHT_CYAN"]+self.thisScriptPath+promptColors["ENDC"]
        #print promptColors["YELLOW"]+_InfoMarkStr_+" current Path "+promptColors["ENDC"] +promptColors["LIGHT_CYAN"]+self.workingPath+promptColors["ENDC"]
        d_dir = []
        f_fileNames = []
        os.chdir(self.thisScriptPath)
        for root, dirs, files in os.walk('./'):
            d_dir = dirs[:]
            break
    
        for _dir in d_dir :
            for e in _extFileNames :
                for f in sorted(glob.glob(os.path.join(_dir, '*.'+e))) :   
                    f = os.path.basename(f)
                    if f == _extExceptFileNames[e] :
                        continue
                    f_fileNames.append(f)
            fileListFromEachDirs.append([_dir,f_fileNames])
            d_dir = []
            f_fileNames = []
        
        fileListFromEachDirs.pop(0)
        print fileListFromEachDirs

def main():
    suker = sukerScript(os.path.dirname(os.path.abspath(__file__)), os.getcwd())
    print _DebugMarkStr_+os.path.dirname(os.path.abspath(__file__))
    print _DebugMarkStr_+__file__
    suker.scriptListGathering()
    suker.conversationLevel1()
    
if __name__ == "__main__":
    try :         
        main()
    finally : 
        pass

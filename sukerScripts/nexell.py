# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 2017

@author: choonghyun.jeon suker
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

suker_commands = [['ssh',['ssh suker@192.168.1.16',
                          'ssh jenkins@192.168.1.26',
                          'ssh nexellstorage@192.168.1.25']],
                  ['git',['git clean -f -d',
                          'git checkout -f']],
                  ['repo',['repo init -u ssh://suker@git.nexell.co.kr:29418/nexell/yocto/manifest',
                           'repo sync',]]
                 ] 

linuxMark = '/'
winMark = '\\'
    
pColors={"BOLD":"\033[1m",
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

_DebugMark_ = "suker Debug ==> "
_InfoMark_ = " ** ==> "

class sukerScript :    
    def __init__(self, path1, path2) :
        self.thisScriptPath = path1
        self.workingPath = path2
        
    def printMenuLevel1(self) :
        #print pColors["YELLOW"]+_InfoMark_+" script Path "+pColors["ENDC"] +pColors["LIGHT_CYAN"]+self.thisScriptPath+pColors["ENDC"]
        #print pColors["YELLOW"]+_InfoMark_+" working Path "+pColors["ENDC"] +pColors["LIGHT_CYAN"]+self.workingPath+pColors["ENDC"]
        print "==============================================================================="
        print pColors["CYAN"]+"Choice script : "+pColors["ENDC"] + pColors["LIGHT_RED"]+"LEVEL 1"+pColors["ENDC"]
        print "==============================================================================="
        print 'select : '
        
        for i in suker_commands :
            print "    "+pColors["GREEN"] + "'"+i[0][0:2]+"'" + ' or ' + "'" + i[0] + "'" + pColors["ENDC"]+" --> search scripts can show or run"
            
        print "\n    "+pColors["GREEN"]+"'q' or 'exit' or 'quit' "+pColors["ENDC"]+" --> Quit this program"
        print "===============================================================================\n"
        
    def printMenuLevel2(self, index) :
        print pColors["YELLOW"]+_InfoMark_+" working Path "+pColors["ENDC"] +pColors["LIGHT_CYAN"]+self.workingPath+pColors["ENDC"]
        print "==============================================================================="
        print pColors["CYAN"]+"Choicet want script "+pColors["ENDC"] + pColors["LIGHT_RED"]+"LEVEL 2"+pColors["ENDC"]
        print "==============================================================================="
        print 'select : '

        cnt = 0
        for i in suker_commands[index][1] :
            print "    "+pColors["LIGHT_RED"] + str(cnt) + ' : ' + i + pColors["ENDC"]+" --> select number..."
            cnt += 1
            
        print "    "+pColors["GREEN"]+"'b'"+pColors["ENDC"]+" --> back menu"
        print "    "+pColors["GREEN"]+"'q' or 'exit' or 'quit'"+pColors["ENDC"]+" --> Quit this program"
        print "===============================================================================\n"
    
    def printScrpitsList(self) :
        print "==============================================================================="
        print "==============================================================================="
        print "select : "+pColors["GREEN"]+"'sc' or 'show'"+pColors["ENDC"]+" --> show git scripts lists"
        print "         "+pColors["GREEN"]+"'b'"+pColors["ENDC"]+" --> back menu"
        print "         "+pColors["GREEN"]+"'q' or 'exit' or 'quit'"+pColors["ENDC"]+" --> Quit this program"
        print "===============================================================================\n"

    #def printUsage() :
    #    print "==========================================================="
    #    print pColors["LIGHT_YELLOW"]+"Select want command"+pColors["ENDC"]+"..."
    #    print "==========================================================="
    #    print "Command : "+pColors["GREEN"]+"'a'"+pColors["ENDC"]+" --> Create dir trees about diff files"
        #print "          "+pColors["GREEN"]+"'b'"+pColors["ENDC"]+" --> tbd"
    #    print "          "+pColors["GREEN"]+"'h'"+pColors["ENDC"]+" or 'help' --> show again Usage"
    #    print "          "+pColors["GREEN"]+"'q'"+pColors["ENDC"]+" or 'exit' or 'quit' --> Quit this program"
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
                for i in suker_commands :
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
                if int(wSpace) < 0 or int(wSpace) >= len(suker_commands[index][1]):
                    print "Fuck You! \n"
                else :
                    self.runningScript(index, int(wSpace))
		    print "\n\n"
                    self.conversationLevel1()
            except ValueError :
                 print "Fuck You! \n"
            
    
    def runningScript(self, dirIndex, runIndex) :
        excuteCmd = suker_commands[dirIndex][1][runIndex]

        print excuteCmd
        os.chdir(self.workingPath)
        try :
            out_bytes = subprocess.call(excuteCmd, shell=True)
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            print out_bytes, code
       

def main():
    suker = sukerScript(os.path.dirname(os.path.abspath(__file__)), os.getcwd())
    print _DebugMark_+os.path.dirname(os.path.abspath(__file__))
    print _DebugMark_+__file__
    suker.conversationLevel1()
    
if __name__ == "__main__":
    try :         
        main()
    finally : 
        pass

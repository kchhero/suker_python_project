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
commandDict = {'q':'QUIT', 'quit':'QUIT', 'exit':'QUIT', 'b':'BACK', 'back':'BACK', 'h':'HELP', 'help':'HELP'}
_extExceptFileNames = {'py':'__init__.py','sh':''}
_extFileNames = ['py','sh']
selectedWorkingSpace = None

suker_commands = [['ssh',['ssh suker@192.168.1.16',
                          'ssh jenkins@192.168.1.26',
                          'ssh nexellstorage@119.65.249.125',
                          'ssh lava-nexell@192.168.1.18',
                          'ssh suker@220.78.49.182',
                          'ssh -X fpga@192.168.1.182',
                         ]
                  ],
                  
                  ['git',['git clean -f -d',
                          'git checkout -f'
                         ]
                  ],
                  
                  ['repo',['repo init -u ssh://suker@git.nexell.co.kr:29418/nexell/yocto/manifest',
                           'repo sync'
                          ]
                  ],
                  
                  ['sudo scp -r',['scp -r <src> <dest>',
                             ''
                            ],
                            ['nexellstorage@192.168.1.25:/home/nexellstorage/snapshot/yocto/',
                             'nexellstorage@192.168.1.25:/home/nexellstorage/releases/NEXELL-YOCTO-SDKs',
                             'jenkins@192.168.1.26:/home/jenkins/Jenkins_Storage/jobs',
                             'jenkins@192.168.1.26:/home/jenkins/Jenkins_Storage/backup_conf',
                            ],
                  ],
                  
                  ['mount', ['sudo mount -t cifs -o user="suker",password="cndgus123",rw,user,exec,auto,file_mode=0755,dir_mode=0755,uid=suker,gid=suker //192.168.1.16/suker ~/sukerSMB',
                             'sudo mount -t cifs //NAS/1st ~/Nexell-NAS1 -o user=nexell,password=nexell,workgroup=WORKGROUP,ip=192.168.1.17,iocharset=utf8',
                             'sudo mount -t cifs //NAS/2nd ~/Nexell-NAS2 -o user=nexell,password=nexell,workgroup=WORKGROUP,ip=192.168.1.17,iocharset=utf8',
                             'sudo mount -t cifs //NAS/3rd ~/Nexell-NAS3 -o user=nexell,password=nexell,workgroup=WORKGROUP,ip=192.168.1.17,iocharset=utf8',
                             'sudo sshfs -p 22 -o allow_other suker@220.78.49.182:/home/suker /home/suker/RISC-V/nexell/soc-reference',
                             'sudo mount /dev/sdb1 /home/suker/sukerSDB',]
                  ],
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
        
    def printMenuLevel3(self, index) :
        print pColors["YELLOW"]+_InfoMark_+" working Path "+pColors["ENDC"] +pColors["LIGHT_CYAN"]+self.workingPath+pColors["ENDC"]
        print "==============================================================================="
        print pColors["CYAN"]+"Choicet want script "+pColors["ENDC"] + pColors["LIGHT_RED"]+"LEVEL 3"+pColors["ENDC"]
        print "==============================================================================="
        print 'select argument : '

        cnt = 0
        for i in suker_commands[index][2] :
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
                    print "Fuck You1 ! \n"
                else :
                    print "Fuck You1 ! \n"
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
                    print "Fuck You 1 ! \n"
    
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
                    print "Fuck You2 ! \n"
                else :
                    if len(suker_commands[index]) > 2 :
                        self.conversationLevel3(index)
                    else:
                        excuteCmd = suker_commands[index][1][int(wSpace)]
                        self.runningScript(excuteCmd)

                    print "\n\n"
                    self.conversationLevel1()
            except ValueError :
                 print "Fuck You 2! \n"


    def conversationLevel3(self, index) :
        self.printMenuLevel3(index)
        wSpace = None
    
        wArg1 = raw_input(_prompt_+"arg1: ").lower()
        wArg2 = raw_input(_prompt_+"arg2: ").lower()
      
        if len(wArg1)==0 or len(wArg2)==0:
            print "Fuck you 3"
            return

        if self.isNumber(wArg1):
            arg1_str = suker_commands[index][2][int(wArg1)]
        else:
            if os.path.exists(wArg1):
                arg1_str = wArg1
            else :
                print "Does not exist " + wArg1
                return

        if self.isNumber(wArg2):
            arg2_str = suker_commands[index][2][int(wArg2)]
        else:
            arg2_str = wArg2
        
        if wArg1 in commandDict.keys() or wArg2 in commandDict.keys() :
            if commandDict[wSpace]=='QUIT' :
                print "GoodBye!! \n"
                sys.exit()
            elif commandDict[wSpace]=='BACK' :
                self.conversationLevel1()
        else :
            _cmd_ = suker_commands[index][0] + ' ' + arg1_str + ' ' + arg2_str
            print 
            try :                
                self.runningScript(_cmd_)
	        print "\n\n"
                self.conversationLevel1()
            except ValueError :
                 print "Fuck You3! \n"


    def runningScript(self, excuteCmd) :
        print pColors["LIGHT_RED"]+"RUN ==> " + excuteCmd + pColors["ENDC"]
        os.chdir(self.workingPath)
        try :
            out_bytes = subprocess.call(excuteCmd, shell=True)
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            print out_bytes, code

    def isNumber(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

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

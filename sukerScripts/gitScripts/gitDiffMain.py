# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:19:47 2014

@author: choonghyun.jeon
"""

import sys
from gitDiffToFiles import *

_prompt_ = " >>> "
WORKING_SPACE = {'a':'android','b':'non_HLOS'}
selectedWorkingSpace = None

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

def printWorkingSpace() :
    print "==========================================================="
    print promptColors["LIGHT_YELLOW"]+"Select your working space "+promptColors["ENDC"]
    print "==========================================================="
    print "select : "+promptColors["GREEN"]+"'a'"+promptColors["ENDC"]+" --> android"
    print "         "+promptColors["GREEN"]+"'b'"+promptColors["ENDC"]+" --> non_HLOS_xxx"
    print "         "+promptColors["GREEN"]+"'q'"+promptColors["ENDC"]+" or 'exit' or 'quit' --> Quit this program"
    print "===========================================================\n"
    
def printUsage() :
    print "==========================================================="
    print promptColors["LIGHT_YELLOW"]+"'___diff_new_dir___'"+promptColors["ENDC"]+" will create your parent dir..."
    print "==========================================================="
    print "Command : "+promptColors["GREEN"]+"'a'"+promptColors["ENDC"]+" --> Create dir trees about diff files"
    #print "          "+promptColors["GREEN"]+"'b'"+promptColors["ENDC"]+" --> tbd"
    print "          "+promptColors["GREEN"]+"'h'"+promptColors["ENDC"]+" or 'help' --> show again Usage"
    print "          "+promptColors["GREEN"]+"'q'"+promptColors["ENDC"]+" or 'exit' or 'quit' --> Quit this program"
    print "===========================================================\n"
    
def conversation() :
    printWorkingSpace()
    wSpace = None
    
    while 1 :
        wSpace = raw_input(_prompt_)
        if wSpace=='q' or wSpace=='quit' or wSpace=='exit' :
            print "GoodBye!! \n"
            sys.exit()
        elif wSpace=='h' or wSpace=='help' :
            printWorkingSpace()
        else :
            selectedWorkingSpace = WORKING_SPACE[wSpace]
            break

    printUsage()    
    usage = None
    
    while 1 :
        usage = raw_input(_prompt_)
        if usage=='q' or usage=='quit' or usage=='exit' :
            print "GoodBye!! \n"
            sys.exit()
        elif usage=='h' or usage=='help' :
            printUsage()
        else :
            gitcntl = gitDiffToFiles(selectedWorkingSpace,promptColors)
            ret = gitcntl.commandGit()
            if ret == True :
                gitcntl.paseGitDiff()

            print " 'h' or 'help' show again usage commands, 'q' or 'quit' exit program."
    
def main():
    conversation()
    
if __name__ == "__main__":
    try :         
        main()
    finally : 
        pass
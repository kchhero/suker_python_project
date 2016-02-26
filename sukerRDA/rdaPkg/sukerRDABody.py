# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 14:24:34 2014

@author: choonghyun.jeon
"""
import string
import re
import mmap
from sukerRDAHH import getDirMark

class abstractorBody():
    DEBUG_ON = False
    
    crashTypeTitle = "Crash Type Select"
    crashTypeList = ["Unknown Crash Type", \
                     "Kernel Crash(Black)", \
                     "Apps Watchdog(Green)", \
                     "DBI Crash(Purple)", \
                     "RPM Crash(Yellow)", \
                     "Modem Crash(Blue)", \
                     "ADSP Crash(Orange)", \
                     "WCNSS Crash(Sky)"]
    crashTypeIdx = 0

    check_buildIdList = ["BOOT.BF","TZ.BF","RPM.BF"]
    parsingListInLK = ["androidboot.hardware", "lge.rev", "lge.bootreason"]
    parsingListInKernel = ["Linux version","UART CONSOLE :","BOARD :","ANDROID BOOT MODE :","Battery :"]   
        
    check_lk_log_mark = "[0] welcome to lk"
    check_kernel_log_START_mark = ""
    check_kernel_log_START_markDict = {0:"Booting Linux on physical CPU 0",
                                       1:"Booting Linux on physical CPU 0x0",
                                       2:"Booting Linux on physical CPU 0x0"}
                                       
    check_android_log_mark = "logger: created 256K log 'log_main'"
    
    easyCrashKeyWord = "] PC is at "
    crashType_Black_keywordL = [easyCrashKeyWord, "] Causing a watchdog bite!"]  #kernel crash normal and kernel crash by watchdog bite   
    crashType_Green_keyword = "] pet_watchdog"
    crashType_Purple_keyword = "] pet_watchdog"
    #crashType_Yellow_keyword = ""
    crashType_Blue_keywordL = ["] Fatal error on the modem.", "] Watchdog bite received from modem software!"]
    crashType_Orange_keyword = "] Fatal error on the ADSP!"
    crashType_Sky_keyword = "] Fatal error on the wcnss."
    
    crashTypeHash = {crashTypeList[1]:crashType_Black_keywordL, \
                     crashTypeList[2]:crashType_Green_keyword, \
                     crashTypeList[3]:crashType_Purple_keyword, \
                     crashTypeList[5]:crashType_Blue_keywordL, \
                     crashTypeList[6]:crashType_Orange_keyword, \
                     crashTypeList[7]:crashType_Sky_keyword}

    crashType_All_keyword1 = [i for i in crashType_Black_keywordL]
    crashType_All_keyword2 = [i for i in crashType_Blue_keywordL]    
    crashType_All_keyword3 = [crashType_Green_keyword, crashType_Purple_keyword, crashType_Orange_keyword, crashType_Sky_keyword]
    crashType_All_keywordsL = crashType_All_keyword1 + crashType_All_keyword2 + crashType_All_keyword3
    
    BIN_0 = "DDRCS0.BIN"
    BIN_1 = "DDRCS1.BIN"
    
    PARSE_STEP1 = 1
    PARSE_STEP1 = 2
    
    KERNEL_CATCH_SIZE = 1024*512  #512KB
    DEFAULT_CATCH_SIZE = 1024*256  #256KB
    LK_LOG_SIZE = 16*1024  #16KB
    ANDROID_LOG_SIZE = 256*1024  #16KB

    #--------------------------------------- for summingup ---------------------------------------
    lkLogFileName = ""
    kernelLogFileName = ""
    crashLogFileName = ""
    androidLogFileName = ""
    etcFileName = ""
    cmmFileName = ""
    #---------------------------------------- for parsing ----------------------------------------
    lk_log = ""
    kernel_log = ""
    crash_log = ""
    etc_log = ""
    android_log = ""
    #---------------------------------------- for parsing ----------------------------------------
    linuxVersion = 0
    
    def __init__(self):
        pass
        
    def createCMM(self, dirPath, name) :
        cLFN = dirPath+name
        with open(cLFN, 'rb') as data:
            m = mmap.mmap(data.fileno(), 0,access=mmap.ACCESS_READ)
            currPos_PC = m.find("pc : ")            
            currPos_R00 = m.find("r0 : ")
            
            m.seek(currPos_PC)
            read512 = m.read(currPos_R00+16-currPos_PC)

        
            patternAddr = re.compile(r"(\w{8})")
            reOut = patternAddr.findall(str(read512), re.I)
            
            m.close()

            #----------------------------------------------------------------
            #   make cmm file
            #----------------------------------------------------------------
            self.cmmFileName = dirPath+"\sukerRDA_t32_script.cmm"        
            cmmFile = file(self.cmmFileName, 'w')            
            cmmFile.write("sys.cpu CORTEXA7\n")
            cmmFile.write("sys.cpu CORTEXA7\n")
            cmmFile.write("sys.up\n")
            cmmFile.write("data.load.binary "+dirPath+"\DDRCS0.BIN 0x0\n")
            cmmFile.write("data.load.binary "+dirPath+"\DDRCS1.BIN 0x20000000\n")
            cmmFile.write("data.load.binary "+dirPath+"\OCIMEM.BIN 0xfe800000\n")
            cmmFile.write("PER.S.F C15:0x2 %L 0xFFFFC000 0x4000 0x4000\n")
            cmmFile.write("mmu.on\n")
            cmmFile.write("mmu.scan\n")
            cmmFile.write("data.load.elf "+dirPath+"\\vmlinux /nocode\n")
            cmmFile.write("task.config c:\\t32\demo\\arm\kernel\linux\linux.t32\n")
            cmmFile.write("menu.reprogram c:\\t32\demo\\arm\kernel\linux\linux.men\n")
            cmmFile.write("task.dtask\n")
            cmmFile.write("v.v  %ASCII %STRING linux_banner\n")
            cmmFile.write("\n")
            cmmFile.write("r.s pc 0x"+reOut[0]+"\n")
            cmmFile.write("r.s r14 0x"+reOut[1]+"\n")
            cmmFile.write("r.s r13 0x"+reOut[3]+"\n")
            cmmFile.write("r.s r12 0x"+reOut[4]+"\n")
            cmmFile.write("r.s r11 0x"+reOut[5]+"\n")
            cmmFile.write("r.s r10 0x"+reOut[6]+"\n")
            cmmFile.write("r.s r9 0x"+reOut[7]+"\n")
            cmmFile.write("r.s r8 0x"+reOut[8]+"\n")
            cmmFile.write("r.s r7 0x"+reOut[9]+"\n")
            cmmFile.write("r.s r6 0x"+reOut[10]+"\n")
            cmmFile.write("r.s r5 0x"+reOut[11]+"\n")
            cmmFile.write("r.s r4 0x"+reOut[12]+"\n")
            cmmFile.write("r.s r3 0x"+reOut[13]+"\n")
            cmmFile.write("r.s r2 0x"+reOut[14]+"\n")
            cmmFile.write("r.s r1 0x"+reOut[15]+"\n")
            cmmFile.write("r.s r0 0x"+reOut[16]+"\n")
            cmmFile.write("\n"+"ENDDO")
            cmmFile.close()

    def logSummingUp(self, logoutCls, dirPath) :
        if len(self.lkLogFileName)<1 or len(self.kernelLogFileName)<1 :
            self.lkLogFileName = dirPath+"\lk_log.txt"
            self.kernelLogFileName = dirPath+"\kernel_log.txt"
            self.etcFileName = dirPath+"\etc_log.txt"
        
        lkListTemp = []
        kernelListTemp = []
        etcListTemp = []
        
        #--------------------------------------lk-----------------------------------------
        try :
            with open(self.lkLogFileName) as data :
                for line in data :
                    for getLK in self.parsingListInLK :
                        if getLK in line and line in lkListTemp :
                            temp = []
                            temp = line.split(' ')
                            for tempGet in temp :
                                if getLK in tempGet and tempGet not in lkListTemp:
                                    lkListTemp.append(tempGet)
                                    lkListTemp.append("\n")
        except IOError :
            print "File open error"
            
        for s in lkListTemp :
            logoutCls.lkWriteOuts(s)
        
        #--------------------------------------kernel-----------------------------------------
        try :
            with open(self.kernelLogFileName) as data :
                for line in data :
                    for getKernel in self.parsingListInKernel :
                        if getKernel in line :
                            indexx = string.find(line, getKernel)
                            temp = line[indexx:].strip()
                            if temp not in kernelListTemp :
                                kernelListTemp.append(line[indexx:].strip())
                                kernelListTemp.append("\n")
        except IOError :
            print "File open error"

        for s in kernelListTemp :
            logoutCls.kernelWriteOuts(s)            

        #--------------------------------------etc-----------------------------------------
        try :
            with open(self.etcFileName) as data :
                for line in data :
                    for getEtc in self.check_buildIdList :
                        if getEtc in line and getEtc not in etcListTemp :
                            indexx = string.find(line, getEtc)
                            etcListTemp.append(line[indexx:].strip())
                            etcListTemp.append("\n")                
        except IOError :
            print "File open error" 
        
        for s in etcListTemp :
            logoutCls.etcWriteOuts(s)
            
       
    def logParsing(self, dirPath, binFileName, acceptEtc=True, step=1, loggingSize=256) :
        self.lkLogFileName = dirPath + getDirMark() + "lk_log.txt"
        self.kernelLogFileName = dirPath + getDirMark() + "kernel_log.txt"
        self.crashLogFileName = dirPath + getDirMark() + "crash_log.txt"
        self.etcFileName = dirPath + getDirMark() + "etc_log.txt"
        self.androidLogFileName = dirPath + getDirMark() + "android_log.txt"
        
        if loggingSize == 0 or loggingSize < 256 :
            getLogSize = self.DEFAULT_CATCH_SIZE
        else :
            getLogSize = loggingSize*1024
            
        start_KERNEL_LOG_PosL = []
        end_KERNEL_LOG_PosL = []
        
        start_CRASH_PosL = []
        end_CRASH_PosL = []        

        start_LK_PosL = []
        end_LK_PosL = []
        
        start_ANDROID_PosL = []
        end_ANDROID_PosL = []
        
        self.lk_log = file(self.lkLogFileName, 'w')
        self.kernel_log = file(self.kernelLogFileName, 'w')
        self.crash_log = file(self.crashLogFileName, 'w')
        self.android_log = file(self.androidLogFileName, 'w')
        
        if acceptEtc==True :
            self.etc_log = file(self.etcFileName, 'w')

        lk_logging_done = False
        kernel_logging_done = False
        android_logging_done = False
                
        with open(dirPath + getDirMark() + binFileName, 'rb') as ddrcs_bin:
            m = mmap.mmap(ddrcs_bin.fileno(), 0,access=mmap.ACCESS_READ)
            currPos = 0
            if step==2 :
                ddrcs_bin.seek(268435456)  #256MB
                
            #-----------------------------------------------------------
            #       CRASH LOG PARSING
            #-----------------------------------------------------------
            if not self.crashTypeIdx==0 :
                if isinstance(self.crashTypeHash[self.crashTypeList[self.crashTypeIdx]], list) :                    
                    for ele in self.crashTypeHash[self.crashTypeList[self.crashTypeIdx]] :                        
                        m.seek(0)
                        ret = self.doParsingCrash(m, ele, start_CRASH_PosL, end_CRASH_PosL, False, getLogSize)
                        if self.DEBUG_ON :
                            print "Crash log step : not select all --->\n"
                            print "    ele = " + ele + "\n"
                            print "    ret = ", ret
                else :            
                    ret = self.doParsingCrash(m, self.crashTypeHash[self.crashTypeList[self.crashTypeIdx]], \
                                              start_CRASH_PosL, end_CRASH_PosL, False, getLogSize)
                    if self.DEBUG_ON :
                        print "Crash log step : not select all --->\n"
                        print "    ele = " + self.crashTypeHash[self.crashTypeList[self.crashTypeIdx]] + "\n"
                        print "    ret = ", ret

            else :  #search all
                for ele in self.crashType_All_keywordsL :
                    m.seek(0)                    
                    ret = self.doParsingCrash(m, ele, start_CRASH_PosL, end_CRASH_PosL, True, getLogSize)
                    if self.DEBUG_ON :
                        print "Crash log step : select all --->\n"
                        print "    ret = ", ret
                    if ret==1 :
                        break
            
            m.seek(0)
            
            #-----------------------------------------------------------
            #               KERNEL LOG PARSING
            #-----------------------------------------------------------
            while kernel_logging_done==False :
                currPos = m.find(self.check_kernel_log_START_mark)
                if not currPos==-1 :
                    start_KERNEL_LOG_PosL.append(currPos-self.KERNEL_CATCH_SIZE/4)
                    end_KERNEL_LOG_PosL.append(currPos+(self.KERNEL_CATCH_SIZE*3)/4)
                    m.seek(currPos+1)
                else :
                    kernel_logging_done = True            
            m.seek(0)

            #-----------------------------------------------------------
            #               LK LOG PARSING
            #-----------------------------------------------------------
            while lk_logging_done==False :
                currPos = m.find(self.check_lk_log_mark)
                if not currPos==-1 :
                    start_LK_PosL.append(currPos)
                    end_LK_PosL.append(currPos+self.LK_LOG_SIZE)    
                    m.seek(currPos+1)
                else :
                    lk_logging_done = True
            m.seek(0)
          
            #-----------------------------------------------------------
            #               ETC LOG PARSING
            #-----------------------------------------------------------          
            if acceptEtc==True :
                for checkOther in self.check_buildIdList :
                    currPos = m.find(checkOther)
                    if not currPos==-1 :
                        m.seek(currPos)
                        tempOtherStr = m.read(1024)
                        break
                
                if len(tempOtherStr) > 0 :
                    l_tempList = tempOtherStr.strip().split(chr(0))
                    tempList = set(l_tempList)
                    #print len(tempList)
                    for t in tempList :
                        for s in self.check_buildIdList :
                            if s in t :
                                indexy = string.find(t, s)
                                tempList2 = t[indexy:].strip().split(chr(0)) 
                                        
                                self.etc_log.write(tempList2[0])
                                self.etc_log.write("\n")
            m.seek(0)
            
            #-----------------------------------------------------------
            #               Android LOG PARSING
            #-----------------------------------------------------------
            while android_logging_done==False :
                currPos = m.find(self.check_android_log_mark)
                if not currPos==-1 :
                    start_ANDROID_PosL.append(currPos)
                    end_ANDROID_PosL.append(currPos+self.ANDROID_LOG_SIZE)    
                    m.seek(currPos+1)
                else :
                    android_logging_done = True
            m.seek(0)
            
            self.crash_log.write("\n-------------------------------------------------- Crash Log Start ------------------------------------------------------\n")
            for i in range(len(start_CRASH_PosL)) :
                m.seek(start_CRASH_PosL[i])                
                self.crash_log.write(m.read(end_CRASH_PosL[i]-start_CRASH_PosL[i]))
            self.crash_log.write("\n--------------------------------------------------- Crash Log End -------------------------------------------------------\n")

            self.kernel_log.write("\n------------------------------------------------- Kernel Log Start -----------------------------------------------------\n")
            for i in range(len(start_KERNEL_LOG_PosL)) :
                m.seek(start_KERNEL_LOG_PosL[i])
                self.kernel_log.write(m.read(end_KERNEL_LOG_PosL[i]-start_KERNEL_LOG_PosL[i])+"\n")
            self.kernel_log.write("\n---------------------------------------------------- Kernel Log End ----------------------------------------------------\n")
            
            self.lk_log.write("\n------------------------------------------------------ LK Log Start ------------------------------------------------------\n")
            for i in range(len(start_LK_PosL)) :
                m.seek(start_LK_PosL[i])        
                self.lk_log.write(m.read(end_LK_PosL[i]-start_LK_PosL[i])+"\n")
            self.lk_log.write("\n--------------------------------------------------------- LK Log End -----------------------------------------------------\n")
            
            self.android_log.write("\n------------------------------------------------------ ANDROID Log Start ------------------------------------------------------\n")
            for i in range(len(start_ANDROID_PosL)) :
                m.seek(start_ANDROID_PosL[i])        
                self.android_log.write(m.read(end_ANDROID_PosL[i]-start_ANDROID_PosL[i])+"\n")
            self.android_log.write("\n------------------------------------------------------- ANDROID Log End -------------------------------------------------------\n")

            self.fileHandleClose(acceptEtc)
            m.close()
            ddrcs_bin.close()
            
    def doParsingCrash(self, m, ele, start_CRASH_PosL, end_CRASH_PosL, isSearchAll=False, getLogSize=2662144) :
        panic_logging_done=False
        while panic_logging_done==False :
            currPos = m.find(ele)
            if currPos==-1 :
                break
            else :
                m.seek(currPos)
                read1Line = m.read(256)     
                if "%s" not in read1Line :
                    start_CRASH_PosL.append(currPos-getLogSize/2)
                    end_CRASH_PosL.append(currPos+getLogSize/2)                    
                    panic_logging_done = True
                    if isSearchAll==True :
                        if self.DEBUG_ON :
                            print "    catch log a line : " + read1Line + "\n"
                            print "    and return 1 \n"
                        return 1
        if isSearchAll==True :
            return 0
        else :
            return int(panic_logging_done)

    def checkOutFiles(self, __os) :
        if __os.path.getsize(self.kernelLogFileName)==0 : #__os.path.getsize(self.lkLogFileName)==0 or 
            return 0
        else :
            return 1

    def setLinuxVersion(self, ver) :
        self.linuxVersion = ver
        self.check_kernel_log_START_mark = self.check_kernel_log_START_markDict[self.linuxVersion]
        
    def fileHandleClose(self, acceptEtc) :
        self.lk_log.close()
        self.kernel_log.close()
        self.crash_log.close()
        self.android_log.close()
        if acceptEtc==True :
            self.etc_log.close() 
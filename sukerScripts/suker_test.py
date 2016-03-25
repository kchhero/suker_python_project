import sys
import re
import os
import struct
import datetime
import array
import string
import bisect
import traceback
import StringIO
from subprocess import *
from optparse import OptionParser
from optparse import OptionGroup
from struct import unpack
from ctypes import *
from print_out import *
from parser_util import register_parser, RamParser

#========================================================
SHARED_IMEM_BASE_MSM8974 = 0xFE800000
SHARED_IMEM_BASE_MSM8916 = 0x08600000
START_OFFSET_MSM8974 = 0x5720
START_OFFSET_MSM8916 = 0x720
START_OFFSET_DEFAULT = 0x3720
SHARED_IMEM_BASE = 0
#========================================================
MSM8916_RPM_MAP_FILE_NAME = "RPM_AAAAANAAR.map"
MSM8916_RPM_DATA_DUMP_FILE_NAME = "DATARAM.BIN"
#========================================================
DEFAUlT_4BYTE = [0xffffffff,0]
BYTE1_15_8 = [0x0000ff00,8]
BYTE1_7_0 = [0x000000ff,0]
BYTE1_23_16 = [0x00ff0000,16]
#========================================================
CrashHandlerInfoTable = {
"GCC_RESET_STATUS":[0x764,DEFAUlT_4BYTE],
"PMIC_PON_REASON":[0x768,BYTE1_15_8],
"PMIC_WARM_RESET_REASON1":[0x76C,BYTE1_15_8],
"PMIC_WARM_RESET_REASON2":[0x76C,BYTE1_7_0],
"PMIC_POFF_REASON1":[0x770,BYTE1_15_8],
"PMIC_POFF_REASON2":[0x768,BYTE1_7_0],
"PON_PBL_STATUS":[0x774,BYTE1_7_0],
"PS_HOLD_RESET_CTL1":[0x774,BYTE1_15_8],
"PS_HOLD_RESET_CTL2":[0x774,BYTE1_23_16],
}
#========================================================
RPM_SymBols_Address = {    #<--- Here!!  add symbol name
"ddr_register_cache":0x00000000,
#"RPM_CLK_BUFFER_A_REQ_data":0x00000000
}
RPM_SymBols_struct = {    #<--- Here!!  add symbol name
"ddr_register_cache":["".join(["I","I","I","I","IIII","IIIIIIIII","IIII"]),
                      ["SCMO_RCH[1]","SCMO_WCH[1]","SCMO_CMD_BUF[1]","DPE_DRAM[1]","BIMC_M_APP[4]","BIMC_M_SYS[9]","BIMC_M_DSP[4]"]]
#"RPM_CLK_BUFFER_A_REQ_data":"".join(["I"])
}
#========================================================
MSM8916_RPM_CODE_BASE_ADDRESS = 0x00200000
MSM8916_RPM_DATA_BASE_ADDRESS = 0x00290000
#========================================================
RPM_SymBols_Data = {
"ddr_register_cache":["I","I","I","I","IIII","IIIIIIIII","IIII"]
}


#475  SHARED_IMEM_BASE + 0x764 - GCC_RESET_STATUS
#476	SHARED_IMEM_BASE + 0x768[15:8] - PMIC PON Reason 1
#477	SHARED_IMEM_BASE + 0x76C[15:8] - PMIC Warm Reset Reason 1
#478	SHARED_IMEM_BASE + 0x76C[7:0] - PMIC Warm Reset Reason 2
#479	SHARED_IMEM_BASE + 0x770[15:8] - PMIC POFF Reason 1
#480	SHARED_IMEM_BASE + 0x770[7:0] - PMIC POFF Reason 2
#481	SHARED_IMEM_BASE + 0x774[7:0] - PON_PBL STATUS
#482	SHARED_IMEM_BASE + 0x774[15:8] - PS_HOLD_RESET_CTL1
#483	SHARED_IMEM_BASE + 0x774[23:16] - PS_HOLD_RESET_CTL2  


@register_parser("--suker-test", "print tzdump information")
class Suker_Test(RamParser):
    def OCIMEM_dump_parse(self, ramdump, file_path, sukerTextFile) :
        sukerTextFile.write(" ====== OCIMEM_dump_parse START ====== \n")
        try:
            ShMemDumpFile = open("{0}/OCIMEM.BIN".format(file_path), "rb")
            #LogDumpFile = open("{0}/DDRCS0.BIN".format(file_path), "rb")
            if ramdump.tz_start == SHARED_IMEM_BASE_MSM8974 :
                SHARED_IMEM_BASE = SHARED_IMEM_BASE_MSM8974
            elif ramdump.tz_start == SHARED_IMEM_BASE_MSM8916 :
                SHARED_IMEM_BASE = SHARED_IMEM_BASE_MSM8916
            else :
                ShMemDumpFile = open("{0}/MSGRAM.BIN".format(file_path), "rb")
                
        except IOError, e:
            sukerTextFile.write("OCIMEM_dump_parse Error! ==>%s\n"%e)
            return
 
        for chit in CrashHandlerInfoTable.keys() :
            offset = CrashHandlerInfoTable[chit][0]
            mask,shift = CrashHandlerInfoTable[chit][1][0], CrashHandlerInfoTable[chit][1][1]
            ShMemDumpFile.seek(offset,0)
            val = (struct.unpack ('<I',ShMemDumpFile.read(4))[0] & mask) >> shift
            print ("%s = 0x%08x"%(chit,val))
            sukerTextFile.write(("%s = 0x%08x"%(chit,val))+"\n")

        sukerTextFile.write(" ====== OCIMEM_dump_parse END ====== \n\n\n")
        ShMemDumpFile.close()


    def RPM_dump_parse(self, ramdump, file_path, sukerTextFile) :
        sukerTextFile.write(" ====== RPM_dump_parse START ====== \n")
        rpmMapFileName = ""
        rpmDataDumpFileName = ""
        rpm_data_offset = 0
        if ramdump.tz_start == SHARED_IMEM_BASE_MSM8916 :
            rpmMapFileName = "{0}/".format(file_path)+MSM8916_RPM_MAP_FILE_NAME
            rpmDataDumpFileName = MSM8916_RPM_DATA_DUMP_FILE_NAME
        elif ramdump.tz_start == SHARED_IMEM_BASE_MSM8974 :
            return
        else :
            return
            
        if len(rpmMapFileName) == 0 or not os.path.exists(rpmMapFileName) :
            sukerTextFile.write(("%s does not exist \n"%rpmMapFileName)+"\n")
            return
            
        with open(rpmMapFileName, 'rt') as data:
            for line in data :
                for s in RPM_SymBols_Address :
                    if s in line :
                        c = re.search(r"0x\w+[a-f0-9]", line)
                        RPM_SymBols_Address[s] = c.group()
                    pass    
    
        if ramdump.tz_start == SHARED_IMEM_BASE_MSM8916 :
            rpm_data_offset = MSM8916_RPM_DATA_BASE_ADDRESS - MSM8916_RPM_CODE_BASE_ADDRESS
        
        rpmDumpFile = open("{0}/".format(file_path)+rpmDataDumpFileName, "rb")
        
        for i in RPM_SymBols_Address.keys() :
            offset = int(RPM_SymBols_Address[i],16) - rpm_data_offset
            
            rpmDumpFile.seek(offset,0)
            g_tt = struct.unpack(RPM_SymBols_struct[i][0],rpmDumpFile.read(struct.calcsize(RPM_SymBols_struct[i][0])))
            sukerTextFile.write(i+"\n")
            start = 0
            for readSize in RPM_SymBols_Data[i] :
                temp = RPM_SymBols_struct[i][1].pop(0)
                for jj in g_tt[start:start+len(readSize)] :
                    temp += str(hex(jj))
                    temp += ' '
                    
                sukerTextFile.write("\t"+temp+"\n")
                start += len(readSize)

        sukerTextFile.write(" ====== RPM_dump_parse END ====== \n")
        rpmDumpFile.close()
        
    def parse(self) :
        sukerTextFile = self.ramdump.open_file("suker_test.txt")
        self.OCIMEM_dump_parse(self.ramdump, self.ramdump.ebi_path, sukerTextFile)
        self.RPM_dump_parse(self.ramdump, self.ramdump.ebi_path, sukerTextFile)
        sukerTextFile.close()
        print_out_str("Parsing result of sukerTest was saved to {0}/sukerTest.txt".format(self.ramdump.outdir))

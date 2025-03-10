#!/usr/bin/env python
# -*- coding: CP949 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Fri Apr 04 14:36:23 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

# begin suker
import os
import sys
import subprocess
import time
from threading import Thread
import ctypes
# end suker

BUTTON_ID_QPST_SAHARA = 18
BUTTON_ID_PARSER = 28
BUTTON_ID_DUMP = 38
BUTTON_ID_VMLINUX = 48
CHECKBOX_ID_ALL = 110
        
class EasyRamdumpParserRunner(wx.Frame):
    linuxMark = '/'
    winMark = '\\'

    INI_MARK_STR_DICT = {}
    MARK_STR_QPST_SAHARA = '<1>'
    MARK_STR_PARSER = '<2>'
    MARK_STR_DUMP ='<3>'
    MARK_STR_VMLINUX = '<4>'
    MARK_STR_C_ALL = '<C<ALL>'

    GAUGE_MAX = 500
    ARG_ALL = " -x "
    OUTDIR_STR = "** out path ==>  "    
    BUSY_STATE = False
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: EasyRamdumpParserRunner.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_qpst_sahara_dir = wx.StaticText(self, wx.ID_ANY, "QPST Sahara Dir")
        self.button_copyToDump = wx.Button(self, wx.ID_ANY, _("Copy To Dump Dir"))
        self.text_ctrl_qpst_sahara_dir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_qpst_sahara_dir = wx.Button(self, wx.ID_ANY, "...")
        self.button_qpst_sahara_dir.SetId(BUTTON_ID_QPST_SAHARA)
        self.label_parser_dir = wx.StaticText(self, wx.ID_ANY, "Ramdump Parser Path")
        self.label_parser_TBD = wx.StaticText(self, wx.ID_ANY, "")
        self.text_ctrl_parser_dir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_parser_open_dir = wx.Button(self, wx.ID_ANY, "...")
        self.button_parser_open_dir.SetId(BUTTON_ID_PARSER)
        self.label_dump_files_dir = wx.StaticText(self, wx.ID_ANY, "Dump Files Path")
        self.label_dump_files_TBD = wx.StaticText(self, wx.ID_ANY, "")
        self.text_ctrl_dump_dir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_dump_dir = wx.Button(self, wx.ID_ANY, "...")
        self.button_dump_dir.SetId(BUTTON_ID_DUMP)
        self.label_vmlinux_dir = wx.StaticText(self, wx.ID_ANY, "Vmlinux Path")
        self.label_vmlinux_dir_TBD = wx.StaticText(self, wx.ID_ANY, "")
        self.text_ctrl_vmlinux_dir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_vmlinux_dir = wx.Button(self, wx.ID_ANY, "...")
        self.button_vmlinux_dir.SetId(BUTTON_ID_VMLINUX)
        self.label_options = wx.StaticText(self, wx.ID_ANY, "   Ramdump options")
        self.checkbox_all = wx.CheckBox(self, wx.ID_ANY, "--everything (All)")
        self.checkbox_all.SetId(CHECKBOX_ID_ALL)
        self.label_info1 = wx.StaticText(self, wx.ID_ANY, "-> default enabled options : ")
        self.label_info2 = wx.StaticText(self, wx.ID_ANY, "-w -d -t -i -q -s and -a -v")
        self.label_outdir = wx.StaticText(self, wx.ID_ANY, self.OUTDIR_STR)
        self.button_run = wx.Button(self, wx.ID_ANY, "RUN")
        self.button_got32 = wx.Button(self, wx.ID_ANY, "Go T32 (sim)")
        self.button_open_dumpDir = wx.Button(self, wx.ID_ANY, "Open Dump Folder")
        self.status_Text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        self.label_MySignature = wx.StaticText(self, wx.ID_ANY, _("  Created by Suker version 0.9.5   since 2014.10.09"))
        self.gauge_xxx = wx.Gauge(self, wx.ID_ANY, self.GAUGE_MAX, style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.label_status = wx.StaticText(self, wx.ID_ANY, _("Ready"), style=wx.ALIGN_CENTRE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnDumpFilesCopy, self.button_copyToDump)
        self.Bind(wx.EVT_BUTTON, self.OnSetPath, self.button_qpst_sahara_dir)
        self.Bind(wx.EVT_BUTTON, self.OnSetPath, self.button_parser_open_dir)
        self.Bind(wx.EVT_BUTTON, self.OnSetPath, self.button_dump_dir)
        self.Bind(wx.EVT_BUTTON, self.OnSetPath, self.button_vmlinux_dir)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxSelect, self.checkbox_all)
        self.Bind(wx.EVT_BUTTON, self.OnParsing, self.button_run)
        self.Bind(wx.EVT_BUTTON, self.OnGoT32, self.button_got32)
        self.Bind(wx.EVT_BUTTON, self.OnOpenFolder, self.button_open_dumpDir)
        # end wxGlade

        #<1>C:\Documents and Settings\All Users\Application Data\Qualcomm\QPST\Sahara\Port_COM9
        #<2>E:\______LogAndDump_____\ramdump_parser_8x26\
        #<3>E:\______LogAndDump_____\W7_TMUS\QE4\178411\dump
        #<4>E:\______LogAndDump_____\W7_TMUS\QE4\vmlinux_user\
        self.checkBoxInit()
        iniFilePath = os.getcwd() + self.getDirMark() + "setup.ini"
        otherCheckBoxState = True
        if os.path.isfile(iniFilePath) :
            try :
                with open(iniFilePath) as data :
                    for line in data :
                        if len(line) <= 1 :
                            continue
                        
                        tempLine1 = (line.split('>'))[1].strip()                     

                        if "<1" in line :
                            self.text_ctrl_qpst_sahara_dir.SetValue(tempLine1)
                            self.INI_MARK_STR_DICT[self.MARK_STR_QPST_SAHARA] = line.strip()
                        elif "<2" in line :
                            self.text_ctrl_parser_dir.SetValue(tempLine1)
                            self.INI_MARK_STR_DICT[self.MARK_STR_PARSER] = line.strip()
                        elif "<3" in line :
                            self.text_ctrl_dump_dir.SetValue(tempLine1)
                            self.INI_MARK_STR_DICT[self.MARK_STR_DUMP] = line.strip()
                        elif "<4" in line :
                            self.text_ctrl_vmlinux_dir.SetValue(tempLine1)
                            self.INI_MARK_STR_DICT[self.MARK_STR_VMLINUX] = line.strip()
                        elif "<C<ALL" in line and '1'==tempLine1 :
                            self.checkbox_all.SetValue(True)
                            self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL] = line.strip()
                            otherCheckBoxState = False

            except IOError :
                print "File open error"
            
            self.workThread = None
            self.gageCount = 1
            self.pos = 0
            
        self.button_run.SetFocus()
        
    def __set_properties(self):
        # begin wxGlade: EasyRamdumpParserRunner.__set_properties
        self.SetTitle("sukerEasyRamdumpParserRunner")
        self.SetSize((640, 536))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self.status_Text.SetMinSize((622, 80))
        self.label_MySignature.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_status.SetBackgroundColour(wx.Colour(142, 35, 35))
        self.label_status.SetForegroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: EasyRamdumpParserRunner.__do_layout
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        MainMainSizer = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        buttons_box = wx.BoxSizer(wx.HORIZONTAL)
        options_box = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_options_right = wx.GridSizer(2, 3, 0, 0)

        vmlinux_dir = wx.BoxSizer(wx.VERTICAL)
        sizer_vmlinux_down = wx.BoxSizer(wx.HORIZONTAL)
        sizer_vmlinux_up = wx.BoxSizer(wx.HORIZONTAL)
        
        dump_dir = wx.BoxSizer(wx.VERTICAL)
        sizer_dump_down = wx.BoxSizer(wx.HORIZONTAL)
        sizer_dump_up = wx.BoxSizer(wx.HORIZONTAL)

        parser_dir = wx.BoxSizer(wx.VERTICAL)
        sizer_parser_down = wx.BoxSizer(wx.HORIZONTAL)
        sizer_parser_dir_up = wx.BoxSizer(wx.HORIZONTAL)

        qpst_sahara_dir = wx.BoxSizer(wx.VERTICAL)
        sizer_qpst_sahara_dir_down = wx.BoxSizer(wx.HORIZONTAL)
        sizer_qpst_sahara_dir_up = wx.BoxSizer(wx.HORIZONTAL)
        sizer_qpst_sahara_dir_up.Add(self.label_qpst_sahara_dir, 7, wx.ALL | wx.ALIGN_BOTTOM, 3)
        sizer_qpst_sahara_dir_up.Add(self.button_copyToDump, 2, wx.ALL | wx.EXPAND, 3)
        qpst_sahara_dir.Add(sizer_qpst_sahara_dir_up, 1, wx.EXPAND, 0)
        sizer_qpst_sahara_dir_down.Add(self.text_ctrl_qpst_sahara_dir, 7, wx.ALL | wx.EXPAND | wx.ALIGN_BOTTOM, 3)
        sizer_qpst_sahara_dir_down.Add(self.button_qpst_sahara_dir, 2, wx.ALL | wx.EXPAND, 3)
        qpst_sahara_dir.Add(sizer_qpst_sahara_dir_down, 1, wx.EXPAND, 0)
        MainMainSizer.Add(qpst_sahara_dir, 12, wx.ALL | wx.EXPAND, 0)

        sizer_parser_dir_up.Add(self.label_parser_dir, 7, wx.ALL | wx.ALIGN_BOTTOM, 3)
        sizer_parser_dir_up.Add(self.label_parser_TBD, 3, wx.ALL, 3)
        parser_dir.Add(sizer_parser_dir_up, 1, wx.ALL | wx.EXPAND, 0)
        sizer_parser_down.Add(self.text_ctrl_parser_dir, 7, wx.ALL | wx.EXPAND, 3)
        sizer_parser_down.Add(self.button_parser_open_dir, 2, wx.ALL | wx.EXPAND, 3)
        parser_dir.Add(sizer_parser_down, 1, wx.EXPAND, 0)
        MainMainSizer.Add(parser_dir, 12, wx.ALL | wx.EXPAND, 0)

        sizer_dump_up.Add(self.label_dump_files_dir, 7, wx.ALL | wx.ALIGN_BOTTOM, 3)
        sizer_dump_up.Add(self.label_dump_files_TBD, 3, wx.ALL, 3)
        dump_dir.Add(sizer_dump_up, 1, wx.EXPAND, 0)
        sizer_dump_down.Add(self.text_ctrl_dump_dir, 7, wx.ALL | wx.EXPAND, 3)
        sizer_dump_down.Add(self.button_dump_dir, 2, wx.ALL | wx.EXPAND, 3)
        dump_dir.Add(sizer_dump_down, 1, wx.EXPAND, 0)
        MainMainSizer.Add(dump_dir, 12, wx.ALL | wx.EXPAND, 0)

        sizer_vmlinux_up.Add(self.label_vmlinux_dir, 7, wx.ALL | wx.ALIGN_BOTTOM, 3)
        sizer_vmlinux_up.Add(self.label_vmlinux_dir_TBD, 3, wx.ALL, 3)
        vmlinux_dir.Add(sizer_vmlinux_up, 1, wx.EXPAND, 0)
        sizer_vmlinux_down.Add(self.text_ctrl_vmlinux_dir, 7, wx.ALL | wx.EXPAND, 3)
        sizer_vmlinux_down.Add(self.button_vmlinux_dir, 2, wx.ALL | wx.EXPAND, 3)
        vmlinux_dir.Add(sizer_vmlinux_down, 1, wx.EXPAND, 0)
        MainMainSizer.Add(vmlinux_dir, 12, wx.ALL | wx.EXPAND, 0)

        options_box.Add(self.label_options, 2, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 2)
        grid_sizer_options_right.Add(self.checkbox_all, 0, wx.ALL, 3)
        grid_sizer_options_right.Add(self.label_info1, 0, wx.ALL | wx.EXPAND, 3)
        grid_sizer_options_right.Add(self.label_info2, 0, wx.ALL | wx.EXPAND, 3)
        grid_sizer_options_right.Add(self.label_outdir, 0, 0, 0)
        options_box.Add(grid_sizer_options_right, 8, wx.ALL | wx.EXPAND, 5)
        MainMainSizer.Add(options_box, 10, wx.ALL | wx.EXPAND, 0)

        buttons_box.Add(self.button_run, 4, wx.ALL | wx.EXPAND, 3)
        buttons_box.Add(self.button_got32, 3, wx.ALL | wx.EXPAND, 3)
        buttons_box.Add(self.button_open_dumpDir, 3, wx.ALL | wx.EXPAND, 3)
        MainMainSizer.Add(buttons_box, 9, wx.ALL | wx.EXPAND, 2)

        MainMainSizer.Add(self.status_Text, 15, wx.ALL | wx.EXPAND, 3)

        sizer_1.Add(self.label_MySignature, 70, wx.ALL | wx.EXPAND, 3)
        sizer_1.Add(self.gauge_xxx, 20, wx.EXPAND, 0)
        sizer_1.Add(self.label_status, 10, wx.ALL | wx.EXPAND, 3)

        MainMainSizer.Add(sizer_1, 4, wx.EXPAND, 0)
        MainSizer.Add(MainMainSizer, 1, wx.EXPAND, 0)
        self.SetSizer(MainSizer)
        self.Layout()
        # end wxGlade

    def allBtnDisable(self) :
        self.BUSY_STATE = True
        self.button_copyToDump.Enable(False)
        self.button_qpst_sahara_dir.Enable(False)
        self.button_parser_open_dir.Enable(False)
        self.button_dump_dir.Enable(False)
        self.button_vmlinux_dir.Enable(False)
        self.button_run.Enable(False)
        self.button_got32.Enable(False)
        self.button_open_dumpDir.Enable(False)
        
    def allBtnEnable(self) :
        self.BUSY_STATE = False
        self.button_copyToDump.Enable(True)
        self.button_qpst_sahara_dir.Enable(True)
        self.button_parser_open_dir.Enable(True)
        self.button_dump_dir.Enable(True)
        self.button_vmlinux_dir.Enable(True)
        self.button_run.Enable(True)
        self.button_got32.Enable(True)
        self.button_open_dumpDir.Enable(True)
    
    def OnDumpFilesCopy(self, event):
        self.allBtnDisable()
        self.label_status.SetLabel("copying...")
        
        qpstSaharaDir = self.text_ctrl_qpst_sahara_dir.GetValue().strip()
        if qpstSaharaDir[-1]=='\\' :
            qpstSaharaDir = qpstSaharaDir.rstrip('\\')
        self.INI_MARK_STR_DICT[self.MARK_STR_QPST_SAHARA] = self.MARK_STR_QPST_SAHARA+qpstSaharaDir

        dumpDir = self.text_ctrl_dump_dir.GetValue().strip()
        if dumpDir[-1]=='\\' :
            dumpDir = dumpDir.rstrip('\\')
        self.INI_MARK_STR_DICT[self.MARK_STR_DUMP] = self.MARK_STR_DUMP+dumpDir
        
        self.savePaths()

        if self.workThread:
            return

        cmd = "xcopy.exe"
        args = "\"" + qpstSaharaDir + "\"" + " " + dumpDir + " " + "/J /Y"
        
        c_CMDS_c = cmd + " " + args
        proc = subprocess.Popen(c_CMDS_c, shell=True)

        self.workThread = WorkThread(self.gageDisplaay, self.totalCount, proc, self.OnCopyFilesDone)
        self.workThread.start()

        event.Skip()

    def OnCopyFilesDone(self) :
        print "OnCopyFilesDone Done!"
        self.gauge_xxx.SetValue(self.GAUGE_MAX)
        self.allBtnEnable()
        self.label_status.SetLabel("Done!")
        time.sleep(3)
        self.gauge_xxx.SetValue(0)
        
    def OnSetPath(self, event):  # wxGlade: AbstractorShell.<event_handler>
        thisId = event.GetId()
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if thisId==BUTTON_ID_QPST_SAHARA :
            dlg.SetPath(self.text_ctrl_qpst_sahara_dir.GetValue())
        elif thisId==BUTTON_ID_PARSER :
            dlg.SetPath(self.text_ctrl_parser_dir.GetValue())            
        elif thisId==BUTTON_ID_DUMP :
            dlg.SetPath(self.text_ctrl_dump_dir.GetValue())
        elif thisId==BUTTON_ID_VMLINUX :
            dlg.SetPath(self.text_ctrl_vmlinux_dir.GetValue())            
        
        if dlg.ShowModal() == wx.ID_OK:
            newPath = dlg.GetPath()
            oldPath = ""
            if thisId==BUTTON_ID_QPST_SAHARA :
                self.INI_MARK_STR_DICT[self.MARK_STR_QPST_SAHARA] = self.MARK_STR_QPST_SAHARA+newPath
                self.text_ctrl_qpst_sahara_dir.SetValue(newPath)
            elif thisId==BUTTON_ID_PARSER :                
                self.text_ctrl_parser_dir.SetValue(newPath)
                self.INI_MARK_STR_DICT[self.MARK_STR_PARSER] = self.MARK_STR_PARSER+newPath
            elif thisId==BUTTON_ID_DUMP :                
                self.text_ctrl_dump_dir.SetValue(newPath)
                self.INI_MARK_STR_DICT[self.MARK_STR_DUMP] = self.MARK_STR_DUMP+newPath
            elif thisId==BUTTON_ID_VMLINUX :                
                self.text_ctrl_vmlinux_dir.SetValue(newPath)
                self.INI_MARK_STR_DICT[self.MARK_STR_VMLINUX] = self.MARK_STR_VMLINUX+newPath

            self.savePaths()
        dlg.Destroy()
        event.Skip()
  
    def savePaths(self) :
        iniFilePath = os.getcwd() + self.getDirMark() + "setup.ini"       
        iniFile = file(iniFilePath, 'w')
        #print "suker------------savePaths before-----\n"
        #print self.INI_MARK_STR_DICT
        #print "suker-----------------\n"
        
        iniFile.write(self.INI_MARK_STR_DICT[self.MARK_STR_QPST_SAHARA]+"\n")
        iniFile.write(self.INI_MARK_STR_DICT[self.MARK_STR_PARSER]+"\n")
        iniFile.write(self.INI_MARK_STR_DICT[self.MARK_STR_DUMP]+"\n")
        iniFile.write(self.INI_MARK_STR_DICT[self.MARK_STR_VMLINUX]+"\n")
        iniFile.write(self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL]+"\n")
        iniFile.close()

        self.label_outdir.SetLabel(self.OUTDIR_STR+self.text_ctrl_dump_dir.GetValue().strip()+"\out")
        #print "suker------------savePaths after-----\n"
        #print self.INI_MARK_STR_DICT
        #print "suker-----------------\n"
        
    def checkBoxInit(self) :
        self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL] = self.MARK_STR_C_ALL+'1'
                
    def OnCheckBoxSelect(self, event):  # wxGlade: MyFrame1.<event_handler>
        if self.BUSY_STATE==True :
            return

        thisId = event.GetId()
        if thisId==CHECKBOX_ID_ALL :
            allChecked = int(self.checkbox_all.IsChecked())
            self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL] = self.MARK_STR_C_ALL+str(allChecked)
        else:
            pass
        
        event.Skip()
        
    def OnParsing(self, event):  # wxGlade: MyFrame1.<event_handler>
        #dump 폴더의 ramparse.bat check하는거 넣어야됨
        self.allBtnDisable()
        self.label_status.SetLabel("doing...")
        
        saharaDir = self.text_ctrl_qpst_sahara_dir.GetValue().strip()
        self.INI_MARK_STR_DICT[self.MARK_STR_QPST_SAHARA] = self.MARK_STR_QPST_SAHARA+saharaDir
            
        parserDir = self.text_ctrl_parser_dir.GetValue().strip()
        if len(parserDir) < 3 :
            self.showExceptMsgBox("RamdumpParser")
        else :            
            if parserDir[-1]=='\\' :
                parserDir = parserDir.rstrip('\\')
            self.INI_MARK_STR_DICT[self.MARK_STR_PARSER] = self.MARK_STR_PARSER+parserDir
        
        dumpDir = self.text_ctrl_dump_dir.GetValue().strip()
        if len(dumpDir) < 3 :
            self.showExceptMsgBox("Dump Files")
        else :
            if dumpDir[-1]=='\\' :
                dumpDir = dumpDir.rstrip('\\')
            self.INI_MARK_STR_DICT[self.MARK_STR_DUMP] = self.MARK_STR_DUMP+dumpDir
        
        vmlinuxDir = self.text_ctrl_vmlinux_dir.GetValue().strip()
        if len(vmlinuxDir) < 3 :
            self.showExceptMsgBox("vmlinux file")
        else :
            if vmlinuxDir[-1]=='\\' :
                vmlinuxDir = vmlinuxDir.rstrip('\\')
            self.INI_MARK_STR_DICT[self.MARK_STR_VMLINUX] = self.MARK_STR_VMLINUX+vmlinuxDir

        if self.workThread:
            return

        cmd = parserDir+self.getDirMark()+"ramparse.py"
        args1 = " -a " + dumpDir + " -v " + vmlinuxDir + self.getDirMark() + "vmlinux" + " -o " + dumpDir + self.getDirMark() + "out"
        args2L = ['-w','-d','-t','-i','-q','-s']
        args2 = ""
        if self.checkbox_all.IsChecked()==True :
            args2 = self.ARG_ALL
            self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL] = self.MARK_STR_C_ALL+'1'            
        else:
            self.INI_MARK_STR_DICT[self.MARK_STR_C_ALL] = self.MARK_STR_C_ALL+'0'

            args2 = " ".join(args2L)        
                
        self.savePaths()
        
        _CMDS_ = cmd + args1 + " " + args2
        os.chdir(parserDir)
#        proc = subprocess.Popen(_CMDS_, shell=True)
        hash_pipe = subprocess.Popen(_CMDS_, shell=True, stdout=None, stderr=subprocess.PIPE)
        
        self.status_Text.Clear()
        self.status_Text.SetValue("--- status ---\n")
        
        self.workThread = WorkThread(self.gageDisplaay, self.totalCount, hash_pipe, self.OnParsingDone, self.status_Text)
        self.workThread.start()

        event.Skip()
    
    def OnParsingDone(self) :
        print "OnParsing Done!"
        self.gauge_xxx.SetValue(self.GAUGE_MAX)
        self.allBtnEnable()
        self.label_status.SetLabel("Done!")
        time.sleep(3)
        self.gauge_xxx.SetValue(0)
        
    def totalCount(self, count) :
        self.gageCount = count
        
    def gageDisplaay(self, pos) :
        self.pos = pos + 1
        self.gauge_xxx.SetValue(self.GAUGE_MAX * self.pos / self.gageCount)
        self.gauge_xxx.Refresh()
        
    def OnGoT32(self, event):
        dumpDir = self.text_ctrl_dump_dir.GetValue().strip()
        if dumpDir[-1]=='\\' :
            dumpDir = dumpDir.rstrip('\\')
            
        t32Path = dumpDir + self.getDirMark() + "launch_t32.bat"
        if os.path.exists(t32Path)==True :
            os.system(t32Path)
        else :
            ctypes.windll.user32.MessageBoxA(0, "Can not find launch_t32.bat", "Error", 1)
        event.Skip()

    def OnOpenFolder(self, event):  # wxGlade: AbstractorShell.<event_handler>
        if os.path.exists(self.text_ctrl_dump_dir.GetValue().strip())==True :
            os.system("explorer "+self.text_ctrl_dump_dir.GetValue().strip())
        else :
            ctypes.windll.user32.MessageBoxA(0, "Can not find dump folder", "Error", 1)

        event.Skip()

    def getDirMark(self) :
        if sys.platform=='linux2' :
            return self.linuxMark
        else :
            return self.winMark

    def showExceptMsgBox(self, msg) :
        ctypes.windll.user32.MessageBoxA(0, "Invalid "+msg+" path! Please Check Again...", "Error", 1)
        
class WorkThread(Thread):
    def __init__(self, gageDisplaay, totalCount, proc, doneProc, textOut):
        Thread.__init__(self)
        self.gageDisplaay = gageDisplaay
        self.totalCount = totalCount
        self.p = proc
        self._done = doneProc
        self.out = textOut
        
    def run(self):        
        self.totalCount(100)
        i = 0
        while self.p.poll() is None :
            #for i in range(100):
            if i < 100 :
                self.gageDisplaay(i+1)
                i += 2
                time.sleep(1)
            #outtt = self.p.stdout.readline()
            outerr = self.p.stderr.readline()
            #self.out.AppendText("..(1)"+outtt)
            self.out.SetInsertionPointEnd()
            self.out.AppendText(outerr)
            self.out.SetInsertionPointEnd()
            #print "(2)"+outerr
        
        # It's done
        #print "Process ended, ret code:", self.p.returncode
        self._done()
        
# end of class EasyRamdumpParserRunner
def main():
    gettext.install("SukerEasyRamdumpParserRunner") # replace with the appropriate catalog name

    SukerRamDumpParserRunner = wx.App(False)  #app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_Main = EasyRamdumpParserRunner(None, wx.ID_ANY, "")
    #icon
    frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
    SukerRamDumpParserRunner.SetTopWindow(frame_Main)
    frame_Main.Show()
    SukerRamDumpParserRunner.MainLoop()
    
if __name__ == "__main__":
    try : 
        #profile.run('main()')
        main()
    finally : 
        pass
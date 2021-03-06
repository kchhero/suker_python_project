#!/usr/bin/env python
# -*- coding: CP949 -*-
#
# created by SUKER on Nov 2013
# re-generated by wxGlade 0.6.8 (standalone edition) on Tue Feb 04 09:21:47 2014
# Using IDE tool : Spyder (Python 2.7), before WING IDE.
# re-factoring 2014/02/06
# crash type appened. 2014/02/07    # parsing 한 log 파일에서 ascii 보고 쓸데없는 문자 정리할것.

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
#import subprocess
import os

from time import localtime, strftime
# end wxGlade

from sukerRDALogOut import logOutputs
from sukerRDAHelp import HelpAboutDialog
from sukerRDAHH import getDirMark
from sukerRDABody import abstractorBody

#import profile

class AbstractorShell(wx.Frame):
    global selectedIndex
    abstractorBodyCls = 0
    logoutCls = 0    
    dirPath = ""
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: AbstractorShell.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER
        wx.Frame.__init__(self, *args, **kwds)

        #sub-class instance create
        self.abstractorBodyCls = abstractorBody()
        self.logoutCls = logOutputs()
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.wxglade_tmp_menu = wx.Menu()
        self.menu_file_exit = wx.MenuItem(self.wxglade_tmp_menu, wx.ID_ANY, "Exit", "x", wx.ITEM_NORMAL)
        self.wxglade_tmp_menu.AppendItem(self.menu_file_exit)
        self.frame_menubar.Append(self.wxglade_tmp_menu, "&File")
        self.wxglade_tmp_menu = wx.Menu()
        self.menu_help_about = wx.MenuItem(self.wxglade_tmp_menu, wx.ID_ANY, "About and Using", "Help for this program", wx.ITEM_NORMAL)
        self.wxglade_tmp_menu.AppendItem(self.menu_help_about)
        self.frame_menubar.Append(self.wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.frame_statusbar = self.CreateStatusBar(1, 0)
        self.label_RamDumpPath = wx.StaticText(self, wx.ID_ANY, " RamDumpPath")
        self.text_ctrl_RamDumpPath = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_upper_right_empty = wx.StaticText(self, wx.ID_ANY, "")
        self.button_RamDumpPath = wx.Button(self, wx.ID_ANY, "...")
        self.radio_box_linuxVer = wx.RadioBox(self, wx.ID_ANY, _("Linux Version"), choices=[_("linux version 3.4.x"), _("linux version 3.7.x"), _("linux version 3.10.x")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.text_ctrl_logs = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        #self.radio_box_crashType = wx.RadioBox(self, wx.ID_ANY, _(crashTypeTitle), choices=[_(crashTypeList[0]), _(crashTypeList[1]), _(crashTypeList[2]), _(crashTypeList[3]), _(crashTypeList[4])], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_crashType = wx.RadioBox(self, wx.ID_ANY, self.abstractorBodyCls.crashTypeTitle, choices=self.abstractorBodyCls.crashTypeList, majorDimension=0, style=wx.RA_SPECIFY_ROWS)        
        self.text_ctrl_log_status = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "   CrashLog Size (KB)")
        self.text_ctrl_logSize = wx.TextCtrl(self, wx.ID_ANY, "256")
        self.button_Run = wx.Button(self, wx.ID_ANY, "Run")
        self.button_OpenDir = wx.Button(self, wx.ID_ANY, "Open log folder")
        self.label_lower_empty1 = wx.StaticText(self, wx.ID_ANY, "")
        self.label_lower_sukerMark = wx.StaticText(self, wx.ID_ANY, "Created by SUKER Version 1.2.0     since Nov. 2013    ", style=wx.ALIGN_RIGHT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnMenuFileExit, self.menu_file_exit)
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAbout, self.menu_help_about)
        self.Bind(wx.EVT_BUTTON, self.OnSetPath, self.button_RamDumpPath)
        self.Bind(wx.EVT_RADIOBOX, self.OnLinuxVerSelect, self.radio_box_linuxVer)
        self.Bind(wx.EVT_RADIOBOX, self.OnRadioSelect, self.radio_box_crashType)
        self.Bind(wx.EVT_BUTTON, self.OnParsing, self.button_Run)
        self.Bind(wx.EVT_BUTTON, self.OnOpenFolder, self.button_OpenDir)
        # end wxGlade

        iniFilePath = os.getcwd() + getDirMark() + "setup.ini"
        if os.path.isfile(iniFilePath) :
            tempInFileRead = []
            try :
                with open(iniFilePath) as data :
                    for line in data :
                        tempInFileRead.append(line)                        
                
                if len(tempInFileRead) == 1 or len(tempInFileRead) == 2:
                    self.dirPath = tempInFileRead[0]
                    self.text_ctrl_RamDumpPath.SetValue(self.dirPath)
                    if len(tempInFileRead) == 2 and isinstance(int(tempInFileRead[1]), int)==True :
                        self.radio_box_linuxVer.SetSelection(int(tempInFileRead[1]))
                        self.button_Run.SetFocus()

            except IOError :
                print "File open error"

    def __set_properties(self):
        # begin wxGlade: AbstractorShell.__set_properties
        self.SetTitle("Suker RamDump Abstractor")
        #_icon = wx.Icon(os.getcwd() + getDirMark() + "sukerRDA.ico", wx.BITMAP_TYPE_ICON)
        #_icon.CopyFromBitmap(wx.Bitmap(os.getcwd() + getDirMark() + "sukerRDA_icon.png", wx.BITMAP_TYPE_ANY))
        #self.SetIcon(_icon)
        self.SetSize((710, 555))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self.frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_statusbar_fields = ["AnHuiNanGoonHyang"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        self.radio_box_linuxVer.SetSelection(2)
        self.text_ctrl_logs.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.radio_box_crashType.SetSelection(0)
        self.text_ctrl_log_status.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_1.SetMinSize((133, 20))
        self.text_ctrl_logSize.SetMinSize((120, 23))
        self.label_lower_sukerMark.SetFont(wx.Font(9, wx.DEFAULT, wx.ITALIC, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AbstractorShell.__do_layout
        sizer_whole = wx.BoxSizer(wx.VERTICAL)
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_lower = wx.BoxSizer(wx.HORIZONTAL)
        sizer_middle = wx.BoxSizer(wx.HORIZONTAL)
        sizer_middle_right = wx.BoxSizer(wx.VERTICAL)
        sizer_middle_left = wx.BoxSizer(wx.VERTICAL)
        sizer_middle_left_lower = wx.BoxSizer(wx.VERTICAL)
        sizer_middle_left_upper = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_upper2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_upper2_left = wx.BoxSizer(wx.HORIZONTAL)
        sizer_upper = wx.BoxSizer(wx.HORIZONTAL)
        sizer_upper_right = wx.BoxSizer(wx.VERTICAL)
        sizer_upper_left = wx.BoxSizer(wx.VERTICAL)
        sizer_upper_left.Add(self.label_RamDumpPath, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_upper_left.Add(self.text_ctrl_RamDumpPath, 0, wx.ALL | wx.EXPAND, 3)
        sizer_upper.Add(sizer_upper_left, 80, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_upper_right.Add(self.label_upper_right_empty, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_upper_right.Add(self.button_RamDumpPath, 0, wx.ALL | wx.EXPAND, 3)
        sizer_upper.Add(sizer_upper_right, 20, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_main.Add(sizer_upper, 10, wx.ALL | wx.EXPAND, 0)
        sizer_upper2_left.Add(self.radio_box_linuxVer, 85, wx.ALL, 0)
        self.sizer_upper2.Add(sizer_upper2_left, 90, wx.ALL | wx.EXPAND, 0)
        sizer_main.Add(self.sizer_upper2, 10, wx.EXPAND, 1)
        sizer_middle_left_upper.Add(self.text_ctrl_logs, 60, wx.ALL | wx.EXPAND, 3)
        sizer_middle_left_upper.Add(self.radio_box_crashType, 30, wx.EXPAND, 0)
        sizer_middle_left.Add(sizer_middle_left_upper, 55, wx.EXPAND, 0)
        sizer_middle_left_lower.Add(self.text_ctrl_log_status, 30, wx.ALL | wx.EXPAND, 3)
        sizer_middle_left.Add(sizer_middle_left_lower, 45, wx.EXPAND, 0)
        sizer_middle.Add(sizer_middle_left, 80, wx.EXPAND, 0)
        sizer_middle_right.Add(self.label_1, 6, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 3)
        sizer_middle_right.Add(self.text_ctrl_logSize, 7, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 4)
        sizer_middle_right.Add(self.button_Run, 40, wx.ALL | wx.EXPAND, 3)
        sizer_middle_right.Add(self.button_OpenDir, 40, wx.ALL | wx.EXPAND, 3)
        sizer_middle.Add(sizer_middle_right, 20, wx.EXPAND, 1)
        sizer_main.Add(sizer_middle, 75, wx.ALL | wx.EXPAND, 0)
        sizer_lower.Add(self.label_lower_empty1, 50, wx.EXPAND, 3)
        sizer_lower.Add(self.label_lower_sukerMark, 50, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_main.Add(sizer_lower, 5, wx.ALL | wx.EXPAND, 0)
        sizer_whole.Add(sizer_main, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_whole)
        self.Layout()
        # end wxGlade

    def OnMenuFileExit(self, event):  # wxGlade: AbstractorShell.<event_handler>
        self.Close(True)

    def OnMenuHelpAbout(self, event):  # wxGlade: AbstractorShell.<event_handler>
        dlg = HelpAboutDialog(self, -1, "")
        dlg.ShowModal()
        dlg.Destroy()
        #event.Skip()

    def OnSetPath(self, event):  # wxGlade: AbstractorShell.<event_handler>
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.text_ctrl_RamDumpPath.SetValue(dlg.GetPath())
            self.saveIniFile()

        dlg.Destroy()
        event.Skip()

    def OnLinuxVerSelect(self, event):
        radioSelected = event.GetEventObject()
        self.curLinuxVer = radioSelected.GetSelection()
        self.saveIniFile()
        event.Skip()

    def saveIniFile(self) :
        iniFile = file(os.getcwd() + getDirMark() + "setup.ini", 'w')
        self.dirPath = self.text_ctrl_RamDumpPath.GetValue()            
        iniFile.write(self.dirPath)
        iniFile.write("\n")
        iniFile.write(str(self.radio_box_linuxVer.GetSelection()))
        iniFile.close()
        
    def OnRadioSelect(self, event):  # wxGlade: AbstractorShell.<event_handler>
        radioSelected = event.GetEventObject()
        self.abstractorBodyCls.crashTypeIdx = radioSelected.GetSelection()
        if self.abstractorBodyCls.crashTypeIdx == 4 :   #RPM Crash parsing impossible
            self.button_Run.Disable()            
            self.text_ctrl_log_status.SetValue("Sorry!, RPM crash type can not parsing. need to be the \".elf\" file. \n")
        else :
            self.button_Run.Enable()
            self.text_ctrl_log_status.SetValue("")
        event.Skip()
    
    def OnParsing(self, event):  # wxGlade: AbstractorShell.<event_handler>
        parsingFile0 = False
        parsingFile1 = False
        
        logSize = self.text_ctrl_logSize.GetValue()
        try :
            logSize = int(logSize)
        except ValueError, n:
            self.text_ctrl_log_status.SetValue("Error!!, Please input Crash Log Size value is integer\n")
            self.text_ctrl_log_status.SetValue(n + "\n")
            event.Skip()
            return
            
        if isinstance(logSize,int) :
            if int(logSize) > 4*1024*1024 or int(logSize) < 1 :
                self.text_ctrl_log_status.SetValue("Error! Crash Log size is very strange\ntoo long or too short\n" + \
                                                   "Propery value is 1byte ~ 4Mbyte \n")
                event.Skip()
                return

        self.saveIniFile()

        #path validation check
        if len(self.dirPath) < 2 :
            self.text_ctrl_logs.SetValue("-------------- Nothing --------------\n")
            self.text_ctrl_log_status.SetValue(strftime("%Y-%m-%d %I:%M:%S", localtime())+">>> Please select the DUMP Folder \n")
        
        else :
            if os.path.exists(self.dirPath)==True:
                self.text_ctrl_logs.Clear()
                self.text_ctrl_log_status.Clear()

                self.abstractorBodyCls.setLinuxVersion(self.radio_box_linuxVer.GetSelection())

                #------------------------------------------------------------------------------------------------------------------
                #       log parsing
                #------------------------------------------------------------------------------------------------------------------
                self.text_ctrl_log_status.SetValue(getCurrentLocalTime() + " >>> RamDump abstraction start! ...\n" +\
                                                    "      Waiting for parsing...\n")                
                #-----------------------------------------------------------
                #       check exist file DDRCS0.bin
                #-----------------------------------------------------------
                if os.path.isfile(self.dirPath+"\DDRCS0.BIN")==False :
                    parsingFile0 = False
                    self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> File not found 'DDRCS0.BIN'...\n")
                    if os.path.isfile(self.dirPath+"\DDRCS1.BIN")==False :
                        parsingFile1 = False
                        self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> File not found 'DDRCS1.BIN'...\n")
                    else :
                        parsingFile1 = True
                else :
                    parsingFile0 = True
                     

                if parsingFile0==True :
                    self.text_ctrl_log_status.AppendText("      Start parsing file => "+ self.abstractorBodyCls.BIN_0 + "...\n")
                    self.abstractorBodyCls.logParsing(self.dirPath, self.abstractorBodyCls.BIN_0, True, self.abstractorBodyCls.PARSE_STEP1, logSize)
                elif parsingFile1==True :
                    self.text_ctrl_log_status.AppendText("      Start parsing file => "+ self.abstractorBodyCls.BIN_1 + "...\n")
                    self.abstractorBodyCls.logParsing(self.dirPath, self.abstractorBodyCls.BIN_1, True, self.abstractorBodyCls.PARSE_STEP1, logSize)
                else :
                    pass
                
                if self.abstractorBodyCls.checkOutFiles(os)==0 : # parsing done but not found anything info.
                    if parsingFile0==True :
                        self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + \
                                                            " >>> Do not find anything in the " + self.abstractorBodyCls.BIN_0 + \
                                                            ", so try " + self.abstractorBodyCls.BIN_1 + " ...\n")
                        self.abstractorBodyCls.logParsing(self.dirPath, self.abstractorBodyCls.BIN_1, False, self.abstractorBodyCls.PARSE_STEP2, logSize)                    

                        if self.abstractorBodyCls.checkOutFiles(os)==0 : # parsing done but not found anything info.
                            self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> Do not Anything.. Recommand you, Give up hahaha! ...\n")

                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> RamDump parsing end! ...\n\n")
                
                #------------------------------------------------------------------------------------------------------------------
                #       log summery
                #------------------------------------------------------------------------------------------------------------------
                self.abstractorBodyCls.logSummingUp(self.logoutCls, self.dirPath)

                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> Logs parsing start! ... \n")    
                    
                self.text_ctrl_logs.SetValue(" ----------  <Device information Summary>  ----------\n\n")
                self.text_ctrl_logs.AppendText(self.logoutCls.getKernelOuts())
                self.text_ctrl_logs.AppendText(self.logoutCls.getLKOuts())
                self.text_ctrl_logs.AppendText(self.logoutCls.getEtcOuts())
                self.logoutCls.allClearList()
                    
                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> Logs parsing end!\n")                
                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " Log files are saved where "+ "'" + self.dirPath+"'"+"\n")
                #------------------------------------------------------------------------------------------------------------------
                #       CMM create
                #------------------------------------------------------------------------------------------------------------------
                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> cmm script creating!\n")
                if os.path.isfile(self.dirPath+"\crash_log.txt")==False :
                    pass
                else :
                    self.abstractorBodyCls.createCMM(self.dirPath,"\crash_log.txt")

                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " >>> cmm script create complete! \n")
                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " Complete! ... \n\n")
                self.text_ctrl_log_status.AppendText(getCurrentLocalTime() + " Click Right Button '"'Open log folder'"' \n")
            #------------------------------------------------------------------------------------------------------------------
            #       dump folder wrong!!
            #------------------------------------------------------------------------------------------------------------------
            else :
                self.text_ctrl_logs.SetValue("-------------- Nothing --------------\n")
                self.text_ctrl_log_status.SetValue(getCurrentLocalTime() + ">>> Please check selected DUMP Folder \n")             

        self.button_Run.Enable()
        self.text_ctrl_logSize.Enable()
        event.Skip()


    def OnOpenFolder(self, event):  # wxGlade: AbstractorShell.<event_handler>
        if os.path.exists(self.dirPath)==True :
            os.system("explorer "+self.dirPath)
        event.Skip()


def getCurrentLocalTime():
    return strftime("%Y-%m-%d %I:%M:%S", localtime())
        
        
def main():
    gettext.install("SukerRamDumpAbstractor") # replace with the appropriate catalog name    
    SukerRamDumpAbstractor = wx.App(False)  #wxPython 2.9   #SukerRamDumpAbstractor = wx.PySimpleApp(0) #wxPython 2.8
    wx.InitAllImageHandlers()
    frame_Main = AbstractorShell(None, wx.ID_ANY, "")
    #icon
    frame_Main.SetIcon(wx.Icon('sukerRDA.ico', wx.BITMAP_TYPE_ICO))
    SukerRamDumpAbstractor.SetTopWindow(frame_Main)
    frame_Main.Show()
    SukerRamDumpAbstractor.MainLoop()

if __name__ == "__main__":
    try : 
        #profile.run('main()')
        main()
    finally : 
        pass

    
"""
print os.path.dirname(os.path.realpath(__file__)) # current file exist dir path
print os.path.realpath(__file__) # current file path ex)suker_RDA.py
"""
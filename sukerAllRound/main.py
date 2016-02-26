#!/usr/bin/env python
# -*- coding: CP949 -*-
import wx
import gettext
#import sys
#from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from sukerNameChanger import nameChanger as nC
from sukerFileListUp import fileListUp as fL
from sukerFastBoot import fastBoot as fb
from sukerRDA2 import sukerRDAMain as rda

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.button_nC = wx.Button(self, wx.ID_ANY, "Name Changer")
        self.button_fastboot = wx.Button(self, wx.ID_ANY, "FastBoot")
        self.button_rda = wx.Button(self, wx.ID_ANY, "RDA2")
        self.button_fileListUp = wx.Button(self, wx.ID_ANY, "File List Up")
        self.button_5 = wx.Button(self, wx.ID_ANY, "TBD")
        self.button_6 = wx.Button(self, wx.ID_ANY, "TBD")
        self.button_7 = wx.Button(self, wx.ID_ANY, "TBD")
        self.button_8 = wx.Button(self, wx.ID_ANY, "TBD")
        self.button_9 = wx.Button(self, wx.ID_ANY, "TBD")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onNameChanger, self.button_nC)
        self.Bind(wx.EVT_BUTTON, self.onFileListUp, self.button_fileListUp)
        self.Bind(wx.EVT_BUTTON, self.onFastBoot, self.button_fastboot)
        self.Bind(wx.EVT_BUTTON, self.onRDA, self.button_rda)        
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("suker AllRound")
        self.SetBackgroundColour(wx.Colour(255, 255, 0))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_main = wx.GridSizer(3, 3, 2, 2)
        grid_sizer_main.Add(self.button_nC, 0, wx.ALL | wx.EXPAND, 3)
        grid_sizer_main.Add(self.button_fastboot, 0, wx.ALL | wx.EXPAND, 3)
        grid_sizer_main.Add(self.button_rda, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_fileListUp, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_5, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_6, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_7, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_8, 0, wx.ALL, 3)
        grid_sizer_main.Add(self.button_9, 0, wx.ALL, 3)
        sizer_main.Add(grid_sizer_main, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_main)
        sizer_main.Fit(self)
        self.Layout()
        # end wxGlade

    def onNameChanger(self, event):  # wxGlade: MyFrame.<event_handler>
        gogo = wx.App(False)  #app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_Main = nC.nameChanger(None, wx.ID_ANY, "")
        #icon
        #frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
        gogo.SetTopWindow(frame_Main)
        frame_Main.Show()
        gogo.MainLoop()
        event.Skip()
        
    def onFileListUp(self, event):  # wxGlade: MyFrame.<event_handler>
        gogo = wx.App(False)  #app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_Main = fL.fileListUp(None, wx.ID_ANY, "")
        #icon
        #frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
        gogo.SetTopWindow(frame_Main)
        frame_Main.Show()
        gogo.MainLoop()
        event.Skip()
        
    def onFastBoot(self, event):  # wxGlade: MyFrame.<event_handler>
        gogo = wx.App(False)  #app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_Main = fb.fastBootMain(None, wx.ID_ANY, "")
        #icon
        #frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
        gogo.SetTopWindow(frame_Main)
        frame_Main.Show()
        gogo.MainLoop()
        event.Skip()
    
    def onRDA(self, event):  # wxGlade: MyFrame.<event_handler>
        gogo = wx.App(False)  #app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_Main = rda.AbstractorShell(None, wx.ID_ANY, "")
        #icon
        #frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
        gogo.SetTopWindow(frame_Main)
        frame_Main.Show()
        gogo.MainLoop()
        event.Skip()    
    
# end of class MyFrame

def main():
    gettext.install("allround") # replace with the appropriate catalog name

    gogo = wx.App(False)  #app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_Main = MyFrame(None, wx.ID_ANY, "")
    #icon
    #frame_Main.SetIcon(wx.Icon('sukerEasyDP.ico', wx.BITMAP_TYPE_ICO))
    gogo.SetTopWindow(frame_Main)
    frame_Main.Show()
    gogo.MainLoop()
    print "main end"
    
if __name__ == "__main__":
    try : 
        main()
    finally : 
        pass
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 14:03:22 2014

@author: choonghyun.jeon
"""
import wx
import os
from sukerRDAHH import getDirMark

class HelpAboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: HelpAboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_about_empty1 = wx.StaticText(self, wx.ID_ANY, "")
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.getcwd() + getDirMark() + "SukerTitle.png", wx.BITMAP_TYPE_ANY))
        self.label_usingExplain = wx.StaticText(self, wx.ID_ANY, "\n1.  \"...\" Button Click >>> Select Ram dump Path\n\n2. \"Run\" Button Click >>> Do Parsing\n\n3. \"Open Log folder\" Button Click >>> parsed log file folder open", style=wx.ST_NO_AUTORESIZE)
        self.label_usingAboutMe = wx.StaticText(self, wx.ID_ANY, "created by suker  version 1.2.0 \nchoonghyun.jeon@lge.com  ", style=wx.ALIGN_RIGHT)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: HelpAboutDialog.__set_properties
        self.SetTitle("About and Using")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(os.getcwd() + getDirMark() + "sukerRDA_icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((400, 300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: HelpAboutDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.label_about_empty1, 5, wx.ALL | wx.EXPAND, 3)
        sizer_2.Add(self.bitmap_1, 30, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.label_usingExplain, 45, wx.ALL | wx.EXPAND | wx.ALIGN_BOTTOM, 5)
        sizer_2.Add(self.label_usingAboutMe, 20, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 5)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade
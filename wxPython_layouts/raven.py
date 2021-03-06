#!/usr/bin/env python
# -*- coding: CP949 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Wed Jun 24 11:17:58 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_Main = wx.Panel(self, wx.ID_ANY)
        self.label_31 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.label_32 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.button_Explore = wx.Button(self.panel_Main, wx.ID_ANY, _("Explore"))
        self.label_33 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.label_34 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.label_35 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.label_36 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.button_ReadyStart = wx.Button(self.panel_Main, wx.ID_ANY, _("Explore Ready,Start"))
        self.button_MainMenu = wx.Button(self.panel_Main, wx.ID_ANY, _("MainMenu"))
        self.button_SelectMap = wx.Button(self.panel_Main, wx.ID_ANY, _("Select Map"))
        self.label_1 = wx.StaticText(self.panel_Main, wx.ID_ANY, "")
        self.button_Again = wx.Button(self.panel_Main, wx.ID_ANY, _("Again"))
        self.button_Next = wx.Button(self.panel_Main, wx.ID_ANY, _("Next Map"))
        self.label_2 = wx.StaticText(self.panel_Main, wx.ID_ANY, _("Created by Suker Version 0.0.1 2015.06.24"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Explore, self.button_Explore)
        self.Bind(wx.EVT_BUTTON, self.ReadyStart, self.button_ReadyStart)
        self.Bind(wx.EVT_BUTTON, self.GoMainMenu, self.button_MainMenu)
        self.Bind(wx.EVT_BUTTON, self.Again, self.button_Again)
        self.Bind(wx.EVT_BUTTON, self.NextMap, self.button_Next)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame_1"))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.SetForegroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.button_Explore.SetMinSize((140, 55))
        self.button_Explore.SetBackgroundColour(wx.Colour(255, 127, 0))
        self.button_ReadyStart.SetBackgroundColour(wx.Colour(79, 107, 255))
        self.button_ReadyStart.SetForegroundColour(wx.Colour(251, 255, 63))
        self.button_MainMenu.SetBackgroundColour(wx.Colour(250, 255, 15))
        self.button_SelectMap.SetBackgroundColour(wx.Colour(12, 99, 10))
        self.button_SelectMap.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_Again.SetBackgroundColour(wx.Colour(255, 143, 250))
        self.button_Next.SetBackgroundColour(wx.Colour(255, 148, 161))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_Main = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.label_31, 1, wx.ALL | wx.EXPAND, 0)
        sizer_5.Add(self.label_32, 1, wx.ALL | wx.EXPAND, 0)
        sizer_5.Add(self.button_Explore, 1, wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_4.Add(self.label_33, 0, wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(self.label_34, 0, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.label_35, 1, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.label_36, 1, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.button_ReadyStart, 3, wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.button_MainMenu, 2, wx.ALL | wx.EXPAND, 0)
        sizer_7.Add(self.button_SelectMap, 2, wx.ALL | wx.EXPAND, 0)
        sizer_7.Add(self.label_1, 1, wx.ALL | wx.EXPAND, 0)
        sizer_7.Add(self.button_Again, 2, wx.ALL | wx.EXPAND, 0)
        sizer_7.Add(self.button_Next, 2, wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_4.Add(self.label_2, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.panel_Main.SetSizer(sizer_4)
        sizer_Main.Add(self.panel_Main, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_Main)
        sizer_Main.Fit(self)
        self.Layout()
        # end wxGlade

    def Explore(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'Explore' not implemented!"
        event.Skip()

    def ReadyStart(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'ReadyStart' not implemented!"
        event.Skip()

    def GoMainMenu(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'GoMainMenu' not implemented!"
        event.Skip()

    def Again(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'Again' not implemented!"
        event.Skip()

    def NextMap(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'NextMap' not implemented!"
        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    RavenFrame = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(RavenFrame)
    RavenFrame.Show()
    app.MainLoop()
#!/usr/bin/env python
# -*- coding: CP949 -*-
#
# generated by wxGlade 0.7.0 on Wed Mar 02 12:15:15 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class sukerStockInfoFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: sukerStockInfoFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.label_Name = wx.StaticText(self, wx.ID_ANY, _("Name"), style=wx.ALIGN_CENTER)
        self.text_ctrl_name0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_code = wx.StaticText(self, wx.ID_ANY, _("Code"), style=wx.ALIGN_CENTER)
        self.text_ctrl_code0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.label_return = wx.StaticText(self, wx.ID_ANY, _("Return"), style=wx.ALIGN_CENTER)
        self.text_ctrl_return0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_current_price = wx.StaticText(self, wx.ID_ANY, _("Current Price"), style=wx.ALIGN_CENTER)
        self.text_ctrl_current_price0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_Numberofshares = wx.StaticText(self, wx.ID_ANY, _("Number of shares"), style=wx.ALIGN_CENTER)
        self.text_ctrl_nos0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_buy_price = wx.StaticText(self, wx.ID_ANY, _("Buy Price"), style=wx.ALIGN_CENTER)
        self.text_ctrl_buy_price0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_profit = wx.StaticText(self, wx.ID_ANY, _("profit"))
        self.text_ctrl_profit0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.button_opensetupfile = wx.Button(self, wx.ID_ANY, _("open setup file"))
        self.label_totalPurchase = wx.StaticText(self, wx.ID_ANY, _("Purchase P."), style=wx.ALIGN_CENTER)
        self.text_ctrl_totalpurchase = wx.TextCtrl(self, wx.ID_ANY, _("8,888,555"), style=wx.TE_READONLY)
        self.label_totalProfit = wx.StaticText(self, wx.ID_ANY, _("Total Profit"), style=wx.ALIGN_CENTER)
        self.text_ctrl_totalProfit = wx.TextCtrl(self, wx.ID_ANY, _("8,888,555"), style=wx.TE_READONLY)
        self.text_ctrl_totaltotal = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.button_refresh = wx.Button(self, wx.ID_ANY, _("Refresh"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.openSetupFile, self.button_opensetupfile)
        self.Bind(wx.EVT_BUTTON, self.refresh, self.button_refresh)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: sukerStockInfoFrame.__set_properties
        self.SetTitle(_("suker Stock Info."))
        self.SetSize((943, 170))
        self.SetBackgroundColour(wx.Colour(35, 142, 35))
        self.label_Name.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_code.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_return.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_current_price.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_Numberofshares.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_buy_price.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_profit.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_totalPurchase.SetForegroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_totalpurchase.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.text_ctrl_totalpurchase.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_totalProfit.SetForegroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_totalProfit.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.text_ctrl_totaltotal.SetBackgroundColour(wx.Colour(127, 255, 0))
        self.button_refresh.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: sukerStockInfoFrame.__do_layout
        self.sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_10.Add(self.label_Name, 0, wx.EXPAND, 1)
        sizer_10.Add(self.text_ctrl_name0, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name1, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name2, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name3, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_10, 16, wx.EXPAND, 0)
        sizer_11.Add(self.label_code, 0, wx.EXPAND, 1)
        sizer_11.Add(self.text_ctrl_code0, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code1, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code2, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code3, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_11, 10, wx.EXPAND, 0)
        sizer_14.Add(self.label_return, 0, wx.EXPAND, 1)
        sizer_14.Add(self.text_ctrl_return0, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return1, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return2, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return3, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_14, 13, wx.EXPAND, 0)
        sizer_12.Add(self.label_current_price, 0, wx.EXPAND, 1)
        sizer_12.Add(self.text_ctrl_current_price0, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price1, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price2, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price3, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_12, 13, wx.EXPAND, 0)
        sizer_2.Add(self.label_Numberofshares, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos0, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos2, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos3, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos4, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_1, 13, wx.EXPAND, 0)
        sizer_13.Add(self.label_buy_price, 0, wx.EXPAND, 1)
        sizer_13.Add(self.text_ctrl_buy_price0, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price1, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price2, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price3, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_13, 13, wx.EXPAND, 0)
        sizer_6.Add(self.label_profit, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_profit0, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_profit1, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_profit2, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_profit3, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_profit4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_6, 13, 0, 0)
        sizer_15.Add(self.button_opensetupfile, 20, wx.ALL | wx.EXPAND, 2)
        sizer_5.Add(self.label_totalPurchase, 0, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.text_ctrl_totalpurchase, 0, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_5, 1, wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(self.label_totalProfit, 0, wx.ALL | wx.EXPAND, 1)
        sizer_4.Add(self.text_ctrl_totalProfit, 0, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_4, 1, wx.ALL | wx.EXPAND, 0)
        sizer_16.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 0)
        sizer_15.Add(sizer_16, 37, wx.ALL | wx.EXPAND, 2)
        sizer_15.Add(self.text_ctrl_totaltotal, 18, wx.ALL | wx.EXPAND, 1)
        sizer_15.Add(self.button_refresh, 25, wx.ALL | wx.EXPAND, 2)
        self.sizer_9.Add(sizer_15, 22, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(self.sizer_9)
        self.Layout()
        # end wxGlade

    def openSetupFile(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        print "Event handler 'openSetupFile' not implemented!"
        event.Skip()

    def refresh(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        print "Event handler 'refresh' not implemented!"
        event.Skip()

# end of class sukerStockInfoFrame

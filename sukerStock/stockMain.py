#!/usr/bin/env python
# -*- coding: CP949 -*-
"""
Created on Mon Feb 29 17:02:28 2016

@author: choonghyun.jeon
"""
import wx
import gettext
from stockBody import stockBodyCls

class sukerStockInfoFrame(wx.Frame):
    sbCls = 0
    sbCls = stockBodyCls()
    
    textCtrlNames = []
    textCtrlCodes = []
    textCtrlCurrentPrices = []
    textCtrlBuyPrices = []
    textCtrlReturnRates = []
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: sukerStockInfoFrame.__init__        
        wx.Frame.__init__(self, *args, **kwds)
        self.label_Name = wx.StaticText(self, wx.ID_ANY, "Name", style=wx.ALIGN_CENTER)
        self.text_ctrl_name0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_name1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_name2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_name3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_name4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_code = wx.StaticText(self, wx.ID_ANY, "Code", style=wx.ALIGN_CENTER)
        self.text_ctrl_code0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_code1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_code2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_code3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_code4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_current_price = wx.StaticText(self, wx.ID_ANY, "Current Price", style=wx.ALIGN_CENTER)
        self.text_ctrl_current_price0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_current_price1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_current_price2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_current_price3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_current_price4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_buy_price = wx.StaticText(self, wx.ID_ANY, "Buy Price", style=wx.ALIGN_CENTER)
        self.text_ctrl_buy_price0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_buy_price1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_buy_price2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_buy_price3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_buy_price4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_return = wx.StaticText(self, wx.ID_ANY, "Return", style=wx.ALIGN_CENTER)
        self.text_ctrl_return0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_return1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_return2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_return3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_return4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_opensetupfile = wx.Button(self, wx.ID_ANY, "open setup file")
        self.label_refreshtime = wx.StaticText(self, wx.ID_ANY, "RefreshTime", style=wx.ALIGN_CENTER)
        self.text_ctrl_refreshtime = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_refresh = wx.Button(self, wx.ID_ANY, "Refresh")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.openSetupFile, self.button_opensetupfile)
        self.Bind(wx.EVT_BUTTON, self.refresh, self.button_refresh)
        # end wxGlade

        self.sbCls.loadIni()
        self.sbCls.stockInfoMaking()
        self.fillVariables()
        if len(self.sbCls.current_prices)>0 :
            self.fillInfo()
        #print sbCls.current_prices
    
    def fillVariables(self) :
        self.textCtrlNames = [self.text_ctrl_name0, self.text_ctrl_name1, self.text_ctrl_name2, self.text_ctrl_name3,
                              self.text_ctrl_name4]
        self.textCtrlCodes = [self.text_ctrl_code0, self.text_ctrl_code1, self.text_ctrl_code2, self.text_ctrl_code3,
                              self.text_ctrl_code4]
        self.textCtrlCurrentPrices = [self.text_ctrl_current_price0, self.text_ctrl_current_price1, self.text_ctrl_current_price2,
                                      self.text_ctrl_current_price3, self.text_ctrl_current_price4]
        self.textCtrlBuyPrices = [self.text_ctrl_buy_price0, self.text_ctrl_buy_price1, self.text_ctrl_buy_price2, 
                                  self.text_ctrl_buy_price3, self.text_ctrl_buy_price4]
        self.textCtrlReturnRates = [self.text_ctrl_return0, self.text_ctrl_return1, self.text_ctrl_return2, self.text_ctrl_return3,
                                    self.text_ctrl_return4]

    def fillInfo(self) :   
        for i in range(0,self.sbCls.index) :                
            if len(self.sbCls.names[i]) > 0 :
                self.textCtrlNames[i].SetValue(self.sbCls.names[i])
                self.textCtrlCodes[i].SetValue(self.sbCls.codes[i])
                self.textCtrlCurrentPrices[i].SetValue(self.sbCls.current_prices[i])
                self.textCtrlBuyPrices[i].SetValue(self.sbCls.prices[i])
                self.textCtrlReturnRates[i].SetValue(self.sbCls.returnRate[i])
        
    def __set_properties(self):
        # begin wxGlade: sukerStockInfoFrame.__set_properties
        self.SetTitle("suker Stock Info.")
        self.SetSize((835, 170))
        self.text_ctrl_current_price0.SetForegroundColour(wx.Colour(255, 0, 0))
        self.text_ctrl_return0.SetForegroundColour(wx.Colour(0, 0, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: sukerStockInfoFrame.__do_layout
        self.sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_10.Add(self.label_Name, 0, wx.EXPAND, 1)
        sizer_10.Add(self.text_ctrl_name0, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name1, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name2, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name3, 0, wx.EXPAND, 0)
        sizer_10.Add(self.text_ctrl_name4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_10, 1, 0, 0)
        sizer_11.Add(self.label_code, 0, wx.EXPAND, 1)
        sizer_11.Add(self.text_ctrl_code0, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code1, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code2, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code3, 0, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_code4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_11, 1, 0, 0)
        sizer_12.Add(self.label_current_price, 0, wx.EXPAND, 1)
        sizer_12.Add(self.text_ctrl_current_price0, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price1, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price2, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price3, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_current_price4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_12, 1, 0, 0)
        sizer_13.Add(self.label_buy_price, 0, wx.EXPAND, 1)
        sizer_13.Add(self.text_ctrl_buy_price0, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price1, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price2, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price3, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_13, 1, 0, 0)
        sizer_14.Add(self.label_return, 0, wx.EXPAND, 1)
        sizer_14.Add(self.text_ctrl_return0, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return1, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return2, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return3, 0, wx.EXPAND, 0)
        sizer_14.Add(self.text_ctrl_return4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_14, 1, 0, 0)
        sizer_15.Add(self.button_opensetupfile, 20, wx.ALL | wx.EXPAND, 2)
        sizer_16.Add(self.label_refreshtime, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 1)
        sizer_16.Add(self.text_ctrl_refreshtime, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 1)
        sizer_15.Add(sizer_16, 30, wx.ALL | wx.EXPAND, 3)
        sizer_15.Add(self.button_refresh, 30, wx.ALL | wx.EXPAND, 2)
        self.sizer_9.Add(sizer_15, 1, 0, 0)
        self.SetSizer(self.sizer_9)
        self.Layout()
        # end wxGlade

    def openSetupFile(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        print "Event handler 'openSetupFile' not implemented!"
        event.Skip()

    def refresh(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        print "Event handler 'refresh' not implemented!"
        event.Skip()
        
    
def main():
    gettext.install("SukerStockInfo") # replace with the appropriate catalog name

    SukerStockInfo = wx.App(False)  #app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_Main = sukerStockInfoFrame(None, wx.ID_ANY, "")
    #icon
    frame_Main.SetIcon(wx.Icon('sukerStock.ico', wx.BITMAP_TYPE_ICO))
    SukerStockInfo.SetTopWindow(frame_Main)
    frame_Main.Show()
    SukerStockInfo.MainLoop()
    
if __name__ == "__main__":
    try : 
        #profile.run('main()')
        main()
    finally : 
        pass



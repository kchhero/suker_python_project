#!/usr/bin/env python
# -*- coding: CP949 -*-
"""
Created on Mon Feb 29 17:02:28 2016

@author: choonghyun.jeon
suker stock info ver 0.1
"""
import wx
import gettext
from stockBody import stockBodyCls
import subprocess

class sukerStockInfoFrame(wx.Frame):
    sbCls = 0
    sbCls = stockBodyCls()
    
    textCtrlNames = []
    textCtrlCodes = []
    textCtrlCurrentPrices = []
    textCtrlBuyPrices = []
    textCtrlReturnRates = []
    textCtrlNumberOfShares = []
    textCtrlProfit = []
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: sukerStockInfoFrame.__init__        
        wx.Frame.__init__(self, *args, **kwds)
        self.label_Name = wx.StaticText(self, wx.ID_ANY, "Name", style=wx.ALIGN_CENTER)
        self.text_ctrl_name0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_name4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_code = wx.StaticText(self, wx.ID_ANY, "Code", style=wx.ALIGN_CENTER)
        self.text_ctrl_code0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.text_ctrl_code4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.label_return = wx.StaticText(self, wx.ID_ANY, "Return", style=wx.ALIGN_CENTER)
        self.text_ctrl_return0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_return4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_current_price = wx.StaticText(self, wx.ID_ANY, "Current Price", style=wx.ALIGN_CENTER)
        self.text_ctrl_current_price0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_current_price4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_Numberofshares = wx.StaticText(self, wx.ID_ANY, "N.O.shares", style=wx.ALIGN_CENTER)
        self.text_ctrl_nos0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_nos4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_buy_price = wx.StaticText(self, wx.ID_ANY, "Buy Price", style=wx.ALIGN_CENTER)
        self.text_ctrl_buy_price0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_buy_price4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_profit = wx.StaticText(self, wx.ID_ANY, "profit", style=wx.ALIGN_CENTER)
        self.text_ctrl_profit0 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit3 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_profit4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.button_opensetupfile = wx.Button(self, wx.ID_ANY, "open setup file")
        self.label_totalPurchase = wx.StaticText(self, wx.ID_ANY, "Purchase P.", style=wx.ALIGN_CENTER)
        self.text_ctrl_totalpurchase = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.label_totalProfit = wx.StaticText(self, wx.ID_ANY, "Total Profit", style=wx.ALIGN_CENTER)
        self.text_ctrl_totalProfit = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RIGHT)
        self.text_ctrl_totaltotal = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.button_refresh = wx.Button(self, wx.ID_ANY, "Refresh")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.openSetupFile, self.button_opensetupfile)
        self.Bind(wx.EVT_BUTTON, self.refresh, self.button_refresh)
        # end wxGlade

        self.fillVariables()
        self.sbCls.loadIni()

        self.doFillInfos()            
        
    def doFillInfos(self) :
        self.sbCls.stockInfoMaking()
        if len(self.sbCls.names[0]) > 0 :
            self.fillInfo()
        
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
        self.textCtrlNumberOfShares = [self.text_ctrl_nos0, self.text_ctrl_nos1, self.text_ctrl_nos2, self.text_ctrl_nos3,
                                       self.text_ctrl_nos4]
        self.textCtrlProfit = [self.text_ctrl_profit0, self.text_ctrl_profit1, self.text_ctrl_profit2, self.text_ctrl_profit3,
                               self.text_ctrl_profit4]
                                       
    def fillInfo(self) :   
        for i in range(0,self.sbCls.index) :
            if len(self.sbCls.names[i]) > 0 :
                self.textCtrlNames[i].SetValue(self.sbCls.names[i])
                self.textCtrlCodes[i].SetValue(self.sbCls.codes[i])
                self.textCtrlCurrentPrices[i].SetValue(self.sbCls.current_prices[i])
                self.textCtrlBuyPrices[i].SetValue(self.sbCls.buyprices[i])
                self.textCtrlReturnRates[i].SetValue(self.sbCls.returnRate[i]+" %") 
                self.textCtrlNumberOfShares[i].SetValue(self.sbCls.numberOfShares[i])
                self.textCtrlProfit[i].SetValue(format(self.sbCls.profit[i],','))
                
        self.text_ctrl_totalProfit.SetValue(format(self.sbCls.totalProfit, ','))
        self.text_ctrl_totalpurchase.SetValue(format(self.sbCls.totalPurchase, ','))
        
        tt = self.sbCls.totalProfit - self.sbCls.totalPurchase
        ttRate = float((tt*100)/self.sbCls.totalPurchase)
        sumTT = format(tt,',') + "  |  " + "%0.2f"%ttRate + " %"
        self.text_ctrl_totaltotal.SetValue(sumTT)
        
        self.changeForegroundColor()
        
    def changeForegroundColor(self) :        
        for i in range(0,self.sbCls.index) :
            if self.sbCls.buyprices[i] < self.sbCls.current_prices[i] :
                self.textCtrlCurrentPrices[i].SetForegroundColour(wx.Colour(255, 0, 0))
                self.textCtrlReturnRates[i].SetForegroundColour(wx.Colour(255, 0, 0))
                self.textCtrlProfit[i].SetForegroundColour(wx.Colour(255,0,0))
            else :
                self.textCtrlCurrentPrices[i].SetForegroundColour(wx.Colour(0, 0, 255))
                self.textCtrlReturnRates[i].SetForegroundColour(wx.Colour(0, 0, 255))
                self.textCtrlProfit[i].SetForegroundColour(wx.Colour(0, 0, 255))
                
        if self.sbCls.totalProfit > 0 :
            self.text_ctrl_totalProfit.SetForegroundColour(wx.Colour(255,0,0))
            self.text_ctrl_totaltotal.SetForegroundColour(wx.Colour(255,0,0))
            
    def __set_properties(self):
        # begin wxGlade: sukerStockInfoFrame.__set_properties
        self.SetTitle("suker Stock Info.")
        self.SetSize((720, 165))
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
        sizer_2.Add(self.label_Numberofshares, 0, wx.EXPAND, 1)
        sizer_2.Add(self.text_ctrl_nos0, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos2, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos3, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_nos4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_2, 10, wx.EXPAND, 0)
        sizer_13.Add(self.label_buy_price, 0, wx.EXPAND, 1)
        sizer_13.Add(self.text_ctrl_buy_price0, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price1, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price2, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price3, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_buy_price4, 0, wx.EXPAND, 0)
        self.sizer_9.Add(sizer_13, 10, wx.EXPAND, 0)
        sizer_6.Add(self.label_profit, 0, wx.EXPAND, 1)
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
        self.sizer_9.Add(sizer_15, 25, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(self.sizer_9)
        self.Layout()
        # end wxGlade

    def openSetupFile(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        #print "Event handler 'openSetupFile' not implemented!"
        path = ""
        dlg = wx.FileDialog(self, "select file path", style=wx.wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

        cmds = "notepad.exe " + path
        proc = subprocess.Popen(cmds, shell=False)
        stdout, stderr = proc.communicate("")
        
        out = str(stdout).decode('utf-8')
        err = str(stderr).decode('utf-8')
        #print "out = ",out
        #print "err = ",err
        
        event.Skip()
        
    def refresh(self, event):  # wxGlade: sukerStockInfoFrame.<event_handler>
        #print "Event handler 'refresh' not implemented!"
        self.doFillInfos() 
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
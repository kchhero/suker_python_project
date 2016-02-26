# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 11:25:31 2014

@author: choonghyun.jeon
"""

class logOutputs():
    lkOut = []
    kernelOut = []
    etcOut = []
    androidOut = []
    
    def __init__(self):
        pass
    
    def lkWriteOuts(self,args) :
        self.lkOut.append(args)
        
    def kernelWriteOuts(self,args) :
        self.kernelOut.append(args)        
    
    def etcWriteOuts(self,args) :
        self.etcOut.append(args)     
    
    def androidWriteOuts(self,args) :
        self.androidOut.append(args)     

    def getLKOuts(self) :
        return "".join(self.lkOut)
    
    def getKernelOuts(self) :
        return "".join(self.kernelOut)
    
    def getEtcOuts(self) :
        return "".join(self.etcOut)
    
    def getAndroidOuts(self) :
        return "".join(self.androidOut)
    
    def allClearList(self) :
        self.lkOut = []
        self.kernelOut = []
        self.etcOut = []
        self.androidOut = []
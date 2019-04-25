# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:00:00 2019

@author: choonghyun.jeon
suker stock info ver 0.1
"""

from stockInfo import stockInfoCls


def main():
    print("main go")


if __name__ == "__main__":
    infoCls = stockInfoCls()
    infoCls.loadIni()
    infoCls.stockInfoMaking()
    infoCls.refresh()

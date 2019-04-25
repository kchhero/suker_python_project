# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:00:00 2018

@author: choonghyun.jeon
suker stock info ver 0.9
"""

from PyQt5 import QtWidgets
from stockInfo import stockInfoCls
from mainwindow import Ui_MainWindow
import subprocess
import os
import sys

useWindowOfMain = {}


def main():
    print()
    # refresh
    # show window


if __name__ == "__main__":
    infoCls = stockInfoCls()
    infoCls.loadIni()
    infoCls.stockInfoMaking()
    print(useWindowOfMain)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.sendInfoClsInst(infoCls)
    ui.do_refresh()

    MainWindow.show()
    sys.exit(app.exec_())

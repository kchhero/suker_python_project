# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\REPOs\kchhero\suker_python_project\sukerStock\sRIMprj\src\stockCrawling_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from stockCrawling_snapshot import stockCrawlingSnapshot as sCS
from stockCrawling_ratio import stockCrawlingRatio as sCR
from stockCrawling_database import stockCrawlingDB as sCDB
from stockCrawling_display import stockCrawlingDisplay as sCDP
from pathlib import Path
import stockConfig as _config_
import pandas as pd

UPDATE_BTN_COMP = 1
UPDATE_BTN_LIST = 2
SHOW_BTN_COMP = 3

class Ui_Dialog(object):
     #---------------------------------------------------------------------
    # class 초기화
    #---------------------------------------------------------------------
    stockCrawlSnapshotCls = sCS("")
    stockCrawlRatioCls = sCR("")
    stockCrawlDBCls = sCDB()
    #stockCrawlDisplayCls = sCDP()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 483)
        self.listView_updatedCompList = QtWidgets.QListView(Dialog)
        self.listView_updatedCompList.setGeometry(QtCore.QRect(510, 60, 281, 381))
        self.listView_updatedCompList.setAutoScroll(False)
        self.listView_updatedCompList.setObjectName("listView_updatedCompList")
        self.plainTextEdit_infoShow = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_infoShow.setGeometry(QtCore.QRect(10, 110, 491, 301))
        self.plainTextEdit_infoShow.setObjectName("plainTextEdit_infoShow")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(496, 60, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 450, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.progressBar_update = QtWidgets.QProgressBar(Dialog)
        self.progressBar_update.setGeometry(QtCore.QRect(10, 420, 491, 23))
        self.progressBar_update.setProperty("value", 24)
        self.progressBar_update.setObjectName("progressBar_update")
        self.pushButton_updateList = QtWidgets.QPushButton(Dialog)
        self.pushButton_updateList.setGeometry(QtCore.QRect(510, 20, 281, 23))
        self.pushButton_updateList.setObjectName("pushButton_updateList")
        self.pushButton_updateCompCode = QtWidgets.QPushButton(Dialog)
        self.pushButton_updateCompCode.setGeometry(QtCore.QRect(20, 60, 161, 31))
        self.pushButton_updateCompCode.setObjectName("pushButton_updateCompCode")
        self.pushButton_compInfoShow = QtWidgets.QPushButton(Dialog)
        self.pushButton_compInfoShow.setGeometry(QtCore.QRect(190, 60, 141, 31))
        self.pushButton_compInfoShow.setObjectName("pushButton_compInfoShow")
        self.textEdit_compCode = QtWidgets.QTextEdit(Dialog)
        self.textEdit_compCode.setGeometry(QtCore.QRect(190, 20, 141, 31))
        self.textEdit_compCode.setAcceptDrops(False)
        self.textEdit_compCode.setAcceptRichText(False)
        self.textEdit_compCode.setObjectName("textEdit_compCode")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #---------------------------------------------------------------------
        # Connect Signal
        #---------------------------------------------------------------------
        #dial.valueChanged.connect(lcd.display)
        self.pushButton_updateCompCode.clicked.connect(self.btnUpdateCompCode)
        self.pushButton_compInfoShow.clicked.connect(self.btnShowCompInfo)
        self.pushButton_updateList.clicked.connect(self.btnUpdateList)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "suker sRIM ver 0.1"))
        self.label.setText(_translate("Dialog", "CopyRight. by suker.  sRIM_suker version 0.1"))
        self.label_2.setText(_translate("Dialog", "종 목 코 드"))
        self.pushButton_updateList.setText(_translate("Dialog", "Update List"))
        self.pushButton_updateCompCode.setText(_translate("Dialog", "UPDATE"))
        self.pushButton_compInfoShow.setText(_translate("Dialog", "SHOW"))
        self.textEdit_compCode.setToolTip(_translate("Dialog", "종목코드입력"))
        #self.pushButton_compInfoShow.setEnabled(False)
        #self.pushButton_updateCompCode.setEnabled(False)
        #self.pushButton_updateList.setEnabled(False)
        
    '''
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    '''

    def btnUpdateCompCode(self) :
        ret = 0
        compCode = self.textEdit_compCode.toPlainText()
        if len(compCode) < 6 :
            self.plainTextEdit_infoShow.setPlainText("Invalid company Code!!")
            return
        
        ret = self.updateInfo(compCode)
        csvFileList = self.fileListUpdate(compCode, False)
        ret = self.stockCrawlDBCls.calculateAndSaveSRIMInfo(csvFileList)
        ret = self.readAndShowInfo(csvFileList)  # display SRIM values in param (true)
        if ret != 0 :
            pass

    def btnShowCompInfo(self) :
        ret = 0
        compCode = "A151860"#self.textEdit_compCode.toPlainText()
        if len(compCode) < 6 :
            self.plainTextEdit_infoShow.setPlainText("Invalid company Code!!")
            return
        csvFileList = self.fileListUpdate(compCode, False)
        ret = self.readAndShowInfo(csvFileList)  # display SRIM values in param (true)
        if ret != 0 :
            pass
        
    def btnUpdateList(self) :
        csvFileList = self.fileListUpdate("", True)
        ret = 0        
        model = QtGui.QStandardItemModel()  
        for i in csvFileList :
            model.appendRow(QtGui.QStandardItem(i))
        self.listView_updatedCompList.setModel(model)

        if ret != 0 :
            pass
    
    def fileListUpdate(self, compCode, isAllUpdate) :
        csvFileList = []
        if isAllUpdate == True :
            for path in Path('.').rglob('../csv/*.csv'):
                temp = path.name
                temp = temp.split('.csv')[0]
                if _config_.FILE_DELIMETER_SNAPSHOT in temp :
                    temp = temp.split(_config_.FILE_DELIMETER_SNAPSHOT)[0]
                elif _config_.FILE_DELIMETER_DATA in temp :
                    temp = temp.split(_config_.FILE_DELIMETER_DATA)[0]
                    
                csvFileList.append(temp.rstrip('_'))
                
            csvFileList = list(set(csvFileList))

        else :
            searchFileCnt = 0
            for path in Path('.').rglob('../csv/*.csv'):
                if compCode in path.name :
                    csvFileList.append("../csv/" + path.name)
                    searchFileCnt += 1
                    if searchFileCnt == 2 :
                        break;

        return csvFileList
    

    def updateInfo(self, compCode) :
        self.stockCrawlSnapshotCls.setCompCode(compCode)
        self.stockCrawlRatioCls.setCompCode(compCode)

        #---------------------------------------------------------------------
        # 종목명, 총 주식수, 자기주식수, 지배주주지분
        #---------------------------------------------------------------------
        self.stockCrawlSnapshotCls.crawlingFNGUIDE_snapshotRun()
        compName = self.stockCrawlSnapshotCls.getCompName()
        totalShareCnt = self.stockCrawlSnapshotCls.getTotalShareCount()
        currentValue = self.stockCrawlSnapshotCls.getCurrentValue()
        compSelfShareCnt = self.stockCrawlSnapshotCls.getCompSelfShareCount()
        shareHoldersList = self.stockCrawlSnapshotCls.getShareHoldersList()
        
        #---------------------------------------------------------------------
        # 결산 연/월, ROE, BPS
        #---------------------------------------------------------------------
        self.stockCrawlRatioCls.crawlingFNGUIDE_financeRatioRun()
        self.stockCrawlRatioCls.crawlingFNGUIDE_investIndexRun()
        yearList = self.stockCrawlRatioCls.getYearList()
        if len(yearList) == 5 :
            yearList.pop(0)
        roeList = self.stockCrawlRatioCls.getROEList()
        if len(roeList) == 5 :
            roeList.pop(0)
        bpsList = self.stockCrawlRatioCls.getBPSList()    
        if len(bpsList) == 5 :
            bpsList.pop(0)
        
        self.stockCrawlDBCls.tableSetup(currentValue, totalShareCnt, compSelfShareCnt,
                                   yearList, roeList, bpsList, shareHoldersList,
                                   compName, compCode)
    
        return 0

    
    def readAndShowInfo(self, csvFileList) :
        _data_ = ""
        _snapshot_ = ""
        
        for i in csvFileList :
            if _config_.FILE_DELIMETER_DATA in i :
                _data_ = pd.read_csv(i, index_col=0)
            if _config_.FILE_DELIMETER_SNAPSHOT in i :
                _snapshot_ = pd.read_csv(i)

        self.plainTextEdit_infoShow.setPlainText("--------------------------------------------")
        self.plainTextEdit_infoShow.appendPlainText("종 목 명 : " + str(_snapshot_[_config_.T_COMPANY_NAME][0]))
        self.plainTextEdit_infoShow.appendPlainText("종목코드 : " + str(_snapshot_[_config_.T_COMPANY_CODE][0]))
        self.plainTextEdit_infoShow.appendPlainText("어제종가 : " + str(_snapshot_[_config_.T_SHARE_PRICE][0]))
        self.plainTextEdit_infoShow.appendPlainText("총주식수 : " + str(_snapshot_[_config_.T_TOTAL_SHARE][0]))
        self.plainTextEdit_infoShow.appendPlainText("자기주식수 : " + str(_snapshot_[_config_.T_SELF_SHARE][0]))
        self.plainTextEdit_infoShow.appendPlainText("--------------------------------------------")
        self.plainTextEdit_infoShow.appendPlainText("sRIM     : " + str(_snapshot_[_config_.T_SRIM][0]))
        self.plainTextEdit_infoShow.appendPlainText("sRIM_w90 : " + str(_snapshot_[_config_.T_SRIM90][0]))
        self.plainTextEdit_infoShow.appendPlainText("sRIM_w80 : " + str(_snapshot_[_config_.T_SRIM80][0]))
        self.plainTextEdit_infoShow.appendPlainText("--------------------------------------------")
        self.plainTextEdit_infoShow.appendPlainText("연결/연도별 지표")
        self.plainTextEdit_infoShow.appendPlainText("--------------------------------------------")
        self.plainTextEdit_infoShow.appendPlainText(str(_data_))
        self.plainTextEdit_infoShow.appendPlainText("--------------------------------------------")
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


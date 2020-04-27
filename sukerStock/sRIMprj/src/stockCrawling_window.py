# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\REPOs\kchhero\suker_python_project\sukerStock\sRIMprj\src\stockCrawling_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
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
    _model_ = QtGui.QStandardItemModel()
    _redColor_ = QtGui.QColor(200, 20, 220)
    _blueColor_ = QtGui.QColor(20, 20, 200)
    _greenColor_ = QtGui.QColor(20, 200, 20)
    _blackColor_ = QtGui.QColor(0, 0, 0)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 483)
        self.listView_updatedCompList = QtWidgets.QListView(Dialog)
        self.listView_updatedCompList.setGeometry(QtCore.QRect(510, 60, 281, 381))
        self.listView_updatedCompList.setAutoScroll(False)
        self.listView_updatedCompList.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.listView_updatedCompList.setTabKeyNavigation(True)
        self.listView_updatedCompList.setAlternatingRowColors(True)
        self.listView_updatedCompList.setObjectName("listView_updatedCompList")
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
        self.label_2.setGeometry(QtCore.QRect(100, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.progressBar_update = QtWidgets.QProgressBar(Dialog)
        self.progressBar_update.setEnabled(False)
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
        self.textEdit_compCode.setGeometry(QtCore.QRect(190, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_compCode.setFont(font)
        self.textEdit_compCode.setAcceptDrops(False)
        self.textEdit_compCode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_compCode.setAutoFillBackground(False)
        self.textEdit_compCode.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_compCode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_compCode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_compCode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_compCode.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_compCode.setTabChangesFocus(True)
        self.textEdit_compCode.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textEdit_compCode.setAcceptRichText(False)
        self.textEdit_compCode.setObjectName("textEdit_compCode")
        self.textEdit_infoShow = QtWidgets.QTextEdit(Dialog)
        self.textEdit_infoShow.setGeometry(QtCore.QRect(10, 100, 491, 311))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.textEdit_infoShow.setFont(font)
        self.textEdit_infoShow.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textEdit_infoShow.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_infoShow.setObjectName("textEdit_infoShow")
        self.tableWidget_compInfo = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_compInfo.setGeometry(QtCore.QRect(20, 290, 411, 111))
        self.tableWidget_compInfo.setAutoFillBackground(False)
        self.tableWidget_compInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_compInfo.setLineWidth(0)
        self.tableWidget_compInfo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_compInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_compInfo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_compInfo.setAutoScroll(False)
        self.tableWidget_compInfo.setAutoScrollMargin(10)
        self.tableWidget_compInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_compInfo.setTabKeyNavigation(False)
        self.tableWidget_compInfo.setProperty("showDropIndicator", False)
        self.tableWidget_compInfo.setDragDropOverwriteMode(False)
        self.tableWidget_compInfo.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_compInfo.setShowGrid(False)
        self.tableWidget_compInfo.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_compInfo.setWordWrap(True)
        self.tableWidget_compInfo.setCornerButtonEnabled(False)
        self.tableWidget_compInfo.setRowCount(3)
        self.tableWidget_compInfo.setColumnCount(5)
        self.tableWidget_compInfo.setObjectName("tableWidget_compInfo")
        self.tableWidget_compInfo.horizontalHeader().setVisible(False)
        self.tableWidget_compInfo.horizontalHeader().setDefaultSectionSize(81)
        self.tableWidget_compInfo.horizontalHeader().setHighlightSections(False)
        self.tableWidget_compInfo.verticalHeader().setVisible(False)
        self.tableWidget_compInfo.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_compInfo.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #---------------------------------------------------------------------
        # Connect Signal
        #---------------------------------------------------------------------
        self.listView_updatedCompList.clicked[QtCore.QModelIndex].connect(self.listViewClicked)
        #dial.valueChanged.connect(lcd.display)
        self.pushButton_updateCompCode.clicked.connect(self.btnUpdateCompCode)
        self.pushButton_compInfoShow.clicked.connect(self.btnShowCompInfo)
        self.pushButton_updateList.clicked.connect(self.btnUpdateList)

        #progress bar timer
        self.timerVar = QtCore.QTimer()
        self.timerVar.setInterval(100)
        self.timerVar.timeout.connect(self.progressBarTimer)        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "suker sRIM ver 0.1"))
        self.label.setText(_translate("Dialog", "CopyRight. by suker.  sRIM_suker version 0.1    "))
        self.label_2.setText(_translate("Dialog", "종 목 코 드"))
        self.pushButton_updateList.setText(_translate("Dialog", "Update List"))
        self.pushButton_updateCompCode.setText(_translate("Dialog", "UPDATE"))
        self.pushButton_compInfoShow.setText(_translate("Dialog", "SHOW"))
        self.textEdit_compCode.setToolTip(_translate("Dialog", "종목코드입력"))
        self.progressBar_update.reset()
        

    def progressBarTimer(self) :
        self.time = self.progressBar_update.value()
        self.time += 1
        self.progressBar_update.setValue(self.time)

        #ProgressBar의 값이 최댓값 이상이 되면 Timer를 중단시켜 ProgressBar의 값이 더이상 증가하지 않게 합니다.
        if self.time >= self.progressBar_update.maximum() :
            self.timerVar.stop()

    def listViewClicked(self, index) :
        item = self._model_.itemFromIndex(index)
        self.textEdit_compCode.setText(item.text().split('_')[-1])
    
    # Update info
    def btnUpdateCompCode(self) :
        self.progressBar_update.reset()
        self.timerVar.start()
        ret = 0
        compCode = self.textEdit_compCode.toPlainText()
        if len(compCode) < 6 :
            self.textEdit_infoShow.setPlainText("Invalid company Code!!")
        else :        
            self.textEdit_infoShow.clear()
            ret = self.updateInfo(compCode)
            csvFileList = self.fileListUpdate(compCode, False)
            print("updateInfo Complete")
            ret = self.readAndShowInfo(csvFileList)  # display SRIM values in param (true)
            if ret != 0 :
                pass

        self.progressBar_update.setValue(self.progressBar_update.maximum())
        self.timerVar.stop()
            
    # Show Info
    def btnShowCompInfo(self) :
        ret = 0
        compCode = self.textEdit_compCode.toPlainText()
        if len(compCode) < 6 :
            self.textEdit_infoShow.setPlainText("Invalid company Code!!")
            return
        csvFileList = self.fileListUpdate(compCode, False)
        ret = self.readAndShowInfo(csvFileList)  # display SRIM values in param (true)
        if ret != 0 :
            pass
        
    # List Update
    def btnUpdateList(self) :
        csvFileList = self.fileListUpdate("", True)
        ret = 0
        self._model_.removeRows(0, self._model_.rowCount())
        for i in csvFileList :
            self._model_.appendRow(QtGui.QStandardItem(i))
        self.listView_updatedCompList.setModel(self._model_)

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
        
        self.stockCrawlDBCls.csvUpdate(currentValue, totalShareCnt, compSelfShareCnt,
                                   yearList, roeList, bpsList, shareHoldersList,
                                   compName, compCode)
    
        return 0

    
    def readAndShowInfo(self, csvFileList) :
        #del [[_data_,_snapshot_]]
        #gc.collect()
        _data_ = pd.DataFrame()
        _snapshot_ = pd.DataFrame()

        for i in csvFileList :
            if _config_.FILE_DELIMETER_DATA in i :
                _data_ = pd.read_csv(i, index_col=0)
            if _config_.FILE_DELIMETER_SNAPSHOT in i :
                _snapshot_ = pd.read_csv(i)

        tempColor = self._blackColor_
        
        if int(_snapshot_[_config_.T_SHARE_PRICE][0]) >= int(_snapshot_[_config_.T_SRIM][0]) :
            tempColor = self._blueColor_
        else :
            tempColor = self._redColor_
            
        self.textEdit_infoShow.setTextColor(self._blackColor_)
        self.textEdit_infoShow.setPlainText("------------------------------------------------------------")
        self.textEdit_infoShow.append("업데이트 : " + str(_snapshot_[_config_.T_UPDATE_DATE][0]))
        self.textEdit_infoShow.append("종 목 명 : " + str(_snapshot_[_config_.T_COMPANY_NAME][0]))
        self.textEdit_infoShow.append("종목코드 : " + str(_snapshot_[_config_.T_COMPANY_CODE][0]))
        self.textEdit_infoShow.setTextColor(self._blueColor_)
        self.textEdit_infoShow.append("어제종가 : " + str(_snapshot_[_config_.T_SHARE_PRICE][0]))
        self.textEdit_infoShow.setTextColor(self._blackColor_)
        self.textEdit_infoShow.append("총주식수 : " + str(_snapshot_[_config_.T_TOTAL_SHARE][0]))
        self.textEdit_infoShow.append("자기주식수 : " + str(_snapshot_[_config_.T_SELF_SHARE][0]))
        self.textEdit_infoShow.append("------------------------------------------------------------")
        self.textEdit_infoShow.setTextColor(tempColor)
        self.textEdit_infoShow.append("sRIM     : " + str(_snapshot_[_config_.T_SRIM][0]))
        self.textEdit_infoShow.setTextColor(self._greenColor_)
        self.textEdit_infoShow.append("sRIM_w90 : " + str(_snapshot_[_config_.T_SRIM90][0]))
        self.textEdit_infoShow.append("sRIM_w80 : " + str(_snapshot_[_config_.T_SRIM80][0]))
        self.textEdit_infoShow.setTextColor(self._blackColor_)
        self.textEdit_infoShow.append("------------------------------------------------------------")
        self.textEdit_infoShow.append("연결/연도별 지표")
        #self.textEdit_infoShow.append("------------------------------------------------------------")
        
        
        #QtTableWidget setting
        temp = str(_data_).split("\n")
        tempIdxList = temp[0].split()
        tempIdxList = [""] + tempIdxList
        self.tableWidget_compInfo.horizontalHeader().setVisible(True)
        self.tableWidget_compInfo.setShowGrid(True)
        self.tableWidget_compInfo.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget_compInfo.setHorizontalHeaderLabels(tempIdxList)
        self.tableWidget_compInfo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget_compInfo.setFrameShadow(QtWidgets.QFrame.Plain)
        style = "::section {""background-color: lightgray; }"
        self.tableWidget_compInfo.horizontalHeader().setStyleSheet(style)
        
        tempROEList = temp[1].split()
        tempBPSList = temp[2].split()
        tempSHSList = temp[3].split()

        # ROE
        item = QtWidgets.QTableWidgetItem(_config_.T_ROE) # create the item
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight) # change the alignment
        self.tableWidget_compInfo.setItem(0, 0, item)        
        # ROE index 0
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempROEList[1])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(0, 1, item)
        # ROE index 1
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempROEList[2])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(0, 2, item)
        # ROE index 2
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempROEList[3])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(0, 3, item)
        # ROE index 3
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempROEList[4])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(0, 4, item)
        
        # BPS
        item = QtWidgets.QTableWidgetItem(_config_.T_BPS) # create the item
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight) # change the alignment
        self.tableWidget_compInfo.setItem(1, 0, item)        
        # BPS index 0
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempBPSList[1])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(1, 1, item)
        # BPS index 1
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempBPSList[2])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(1, 2, item)
        # BPS index 2
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempBPSList[3])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(1, 3, item)
        # BPS index 3
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempBPSList[4])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(1, 4, item)
        
        # ShareHolders
        item = QtWidgets.QTableWidgetItem(_config_.T_SHARE_HOLDERS) # create the item
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight) # change the alignment
        self.tableWidget_compInfo.setItem(2, 0, item)        
        # ShareHolders index 0
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempSHSList[1])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(2, 1, item)
        # ShareHolders index 1
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempSHSList[2])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(2, 2, item)
        # ShareHolders index 2
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempSHSList[3])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(2, 3, item)
        # ShareHolders index 3
        item = QtWidgets.QTableWidgetItem(QtWidgets.QTableWidgetItem(str(tempSHSList[4])))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tableWidget_compInfo.setItem(2, 4, item)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    #sys.exit(app.exec_())
    app.exec_()

    
if __name__ == "__main__":
    main()
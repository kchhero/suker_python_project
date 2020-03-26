# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\REPOs\kchhero\suker_python_project\sukerStock\sRIMprj\src\stockCrawling_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        self.tableWidget_compInfo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget_compInfo.setFrameShadow(QtWidgets.QFrame.Plain)
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
        self.tableWidget_compInfo.horizontalHeader().setVisible(True)
        self.tableWidget_compInfo.horizontalHeader().setDefaultSectionSize(81)
        self.tableWidget_compInfo.horizontalHeader().setHighlightSections(False)
        self.tableWidget_compInfo.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget_compInfo.verticalHeader().setVisible(False)
        self.tableWidget_compInfo.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_compInfo.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "suker sRIM ver 0.1"))
        self.label.setText(_translate("Dialog", "CopyRight. by suker.  sRIM_suker version 0.1    "))
        self.label_2.setText(_translate("Dialog", "종 목 코 드"))
        self.pushButton_updateList.setText(_translate("Dialog", "Update List"))
        self.pushButton_updateCompCode.setText(_translate("Dialog", "UPDATE"))
        self.pushButton_compInfoShow.setText(_translate("Dialog", "SHOW"))
        self.textEdit_compCode.setToolTip(_translate("Dialog", "종목코드입력"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


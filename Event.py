# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Event.ui'
#
# Created: Sat Sep 23 21:24:57 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(459, 317)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lstCountries = QtGui.QListWidget(self.centralwidget)
        self.lstCountries.setGeometry(QtCore.QRect(10, 110, 181, 121))
        self.lstCountries.setObjectName(_fromUtf8("lstCountries"))
        self.ePeriod = QtGui.QLineEdit(self.centralwidget)
        self.ePeriod.setGeometry(QtCore.QRect(10, 60, 431, 20))
        self.ePeriod.setObjectName(_fromUtf8("ePeriod"))
        self.eEvent = QtGui.QLineEdit(self.centralwidget)
        self.eEvent.setGeometry(QtCore.QRect(210, 110, 231, 20))
        self.eEvent.setObjectName(_fromUtf8("eEvent"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(210, 160, 141, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.cbPeriod = QtGui.QCheckBox(self.centralwidget)
        self.cbPeriod.setGeometry(QtCore.QRect(370, 160, 70, 17))
        self.cbPeriod.setObjectName(_fromUtf8("cbPeriod"))
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 200, 141, 22))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.lblCountries = QtGui.QLabel(self.centralwidget)
        self.lblCountries.setGeometry(QtCore.QRect(10, 90, 46, 13))
        self.lblCountries.setObjectName(_fromUtf8("lblCountries"))
        self.lblEvent = QtGui.QLabel(self.centralwidget)
        self.lblEvent.setGeometry(QtCore.QRect(210, 90, 46, 13))
        self.lblEvent.setObjectName(_fromUtf8("lblEvent"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 240, 75, 31))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.btnDelete = QtGui.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(90, 240, 75, 31))
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.btnChoose = QtGui.QPushButton(self.centralwidget)
        self.btnChoose.setGeometry(QtCore.QRect(210, 30, 231, 23))
        self.btnChoose.setObjectName(_fromUtf8("btnChoose"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd MMMM yyyy", None))
        self.cbPeriod.setText(_translate("MainWindow", "Periodical", None))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "dd MMMM yyyy", None))
        self.lblCountries.setText(_translate("MainWindow", "Countries", None))
        self.lblEvent.setText(_translate("MainWindow", "Event", None))
        self.label_3.setText(_translate("MainWindow", "Period", None))
        self.btnAdd.setText(_translate("MainWindow", "Add", None))
        self.btnDelete.setText(_translate("MainWindow", "Delete", None))
        self.btnChoose.setText(_translate("MainWindow", "Choose", None))


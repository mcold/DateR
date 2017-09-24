# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Event.ui'
#
# Created: Sun Sep 24 22:04:22 2017
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

class Ui_ActionWindow(object):
    def setupUi(self, ActionWindow):
        ActionWindow.setObjectName(_fromUtf8("ActionWindow"))
        ActionWindow.resize(459, 322)
        self.centralwidget = QtGui.QWidget(ActionWindow)
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
        self.dateEdit.setMinimumDate(QtCore.QDate(1753, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.cbPeriod = QtGui.QCheckBox(self.centralwidget)
        self.cbPeriod.setGeometry(QtCore.QRect(370, 160, 70, 17))
        self.cbPeriod.setObjectName(_fromUtf8("cbPeriod"))
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 200, 141, 22))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setMinimumDate(QtCore.QDate(1753, 1, 1))
        self.dateEdit_2.setCalendarPopup(True)
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
        self.btnInsert = QtGui.QPushButton(self.centralwidget)
        self.btnInsert.setGeometry(QtCore.QRect(250, 250, 100, 40))
        self.btnInsert.setObjectName(_fromUtf8("btnInsert"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(350, 250, 100, 40))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        #ActionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ActionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #ActionWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ActionWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #ActionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ActionWindow)
        QtCore.QMetaObject.connectSlotsByName(ActionWindow)

    def retranslateUi(self, ActionWindow):
        ActionWindow.setWindowTitle(_translate("ActionWindow", "Action", None))
        self.dateEdit.setDisplayFormat(_translate("ActionWindow", "dd MMMM yyyy", None))
        self.cbPeriod.setText(_translate("ActionWindow", "Periodical", None))
        self.dateEdit_2.setDisplayFormat(_translate("ActionWindow", "dd MMMM yyyy", None))
        self.lblCountries.setText(_translate("ActionWindow", "Countries", None))
        self.lblEvent.setText(_translate("ActionWindow", "Event", None))
        self.label_3.setText(_translate("ActionWindow", "Period", None))
        self.btnAdd.setText(_translate("ActionWindow", "Add", None))
        self.btnDelete.setText(_translate("ActionWindow", "Delete", None))
        self.btnChoose.setText(_translate("ActionWindow", "Choose", None))
        self.btnInsert.setText(_translate("ActionWindow", "Insert", None))
        self.btnClear.setText(_translate("ActionWindow", "Clear", None))


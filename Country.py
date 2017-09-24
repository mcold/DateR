# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Country.ui'
#
# Created: Sat Sep 23 20:31:11 2017
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(602, 360)
        self.lstCountries = QtGui.QListWidget(Form)
        self.lstCountries.setGeometry(QtCore.QRect(10, 30, 211, 271))
        self.lstCountries.setObjectName(_fromUtf8("lstCountries"))
        self.btnAdd = QtGui.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(230, 310, 101, 41))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.btnDelete = QtGui.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(340, 310, 101, 41))
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.btnChoose = QtGui.QPushButton(Form)
        self.btnChoose.setGeometry(QtCore.QRect(450, 310, 141, 41))
        self.btnChoose.setObjectName(_fromUtf8("btnChoose"))
        self.lstEvent = QtGui.QListWidget(Form)
        self.lstEvent.setGeometry(QtCore.QRect(230, 30, 361, 271))
        self.lstEvent.setObjectName(_fromUtf8("lstEvent"))
        self.lblCountries = QtGui.QLabel(Form)
        self.lblCountries.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.lblCountries.setObjectName(_fromUtf8("lblCountries"))
        self.eEvents = QtGui.QLabel(Form)
        self.eEvents.setGeometry(QtCore.QRect(230, 10, 46, 13))
        self.eEvents.setObjectName(_fromUtf8("eEvents"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnAdd.setText(_translate("Form", "Add", None))
        self.btnDelete.setText(_translate("Form", "Delete", None))
        self.btnChoose.setText(_translate("Form", "Choose", None))
        self.lblCountries.setText(_translate("Form", "Countries", None))
        self.eEvents.setText(_translate("Form", "Events", None))


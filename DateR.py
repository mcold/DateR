# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DateR.ui'
#
# Created: Sun Sep 24 22:31:07 2017
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

class Ui_DaterForm(object):
    def setupUi(self, DaterForm):
        DaterForm.setObjectName(_fromUtf8("DaterForm"))
        DaterForm.resize(675, 415)
        self.centralwidget = QtGui.QWidget(DaterForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 25, 441, 341))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.lblCountry = QtGui.QLabel(self.centralwidget)
        self.lblCountry.setGeometry(QtCore.QRect(10, 29, 39, 16))
        self.lblCountry.setObjectName(_fromUtf8("lblCountry"))
        self.lblPeriod = QtGui.QLabel(self.centralwidget)
        self.lblPeriod.setGeometry(QtCore.QRect(10, 55, 30, 16))
        self.lblPeriod.setObjectName(_fromUtf8("lblPeriod"))
        self.lblPerson = QtGui.QLabel(self.centralwidget)
        self.lblPerson.setGeometry(QtCore.QRect(10, 80, 33, 16))
        self.lblPerson.setObjectName(_fromUtf8("lblPerson"))
        self.lblStart = QtGui.QLabel(self.centralwidget)
        self.lblStart.setGeometry(QtCore.QRect(10, 110, 24, 16))
        self.lblStart.setObjectName(_fromUtf8("lblStart"))
        self.lblFinish = QtGui.QLabel(self.centralwidget)
        self.lblFinish.setGeometry(QtCore.QRect(10, 135, 27, 16))
        self.lblFinish.setObjectName(_fromUtf8("lblFinish"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 27, 135, 126))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.eCountry = QtGui.QLineEdit(self.widget)
        self.eCountry.setAlignment(QtCore.Qt.AlignCenter)
        self.eCountry.setObjectName(_fromUtf8("eCountry"))
        self.verticalLayout.addWidget(self.eCountry)
        self.ePeriod = QtGui.QLineEdit(self.widget)
        self.ePeriod.setAlignment(QtCore.Qt.AlignCenter)
        self.ePeriod.setObjectName(_fromUtf8("ePeriod"))
        self.verticalLayout.addWidget(self.ePeriod)
        self.ePerson = QtGui.QLineEdit(self.widget)
        self.ePerson.setAlignment(QtCore.Qt.AlignCenter)
        self.ePerson.setObjectName(_fromUtf8("ePerson"))
        self.verticalLayout.addWidget(self.ePerson)
        self.dateEdit = QtGui.QDateEdit(self.widget)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setDate(QtCore.QDate(1753, 1, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.dateEdit_2 = QtGui.QDateEdit(self.widget)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setDate(QtCore.QDate(1753, 1, 1))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.verticalLayout.addWidget(self.dateEdit_2)
        #DaterForm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DaterForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #DaterForm.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DaterForm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #DaterForm.setStatusBar(self.statusbar)

        self.retranslateUi(DaterForm)
        QtCore.QMetaObject.connectSlotsByName(DaterForm)

    def retranslateUi(self, DaterForm):
        DaterForm.setWindowTitle(_translate("DaterForm", "DateR", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DaterForm", "Action", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DaterForm", "Start", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DaterForm", "Date", None))
        self.lblCountry.setText(_translate("DaterForm", "Country", None))
        self.lblPeriod.setText(_translate("DaterForm", "Period", None))
        self.lblPerson.setText(_translate("DaterForm", "Person", None))
        self.lblStart.setText(_translate("DaterForm", "Start", None))
        self.lblFinish.setText(_translate("DaterForm", "Finish", None))


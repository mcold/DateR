# coding: utf-8

from PyQt4 import QtGui, QtCore
import sys
import os.path
from DateR import Ui_DaterForm
from Country import Ui_Form
from Event import Ui_ActionWindow
from db import _db

class DaterForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DaterForm()
        self.ui.setupUi(self)
        self.db = _db()


class ActionForm(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_ActionWindow()
        self.ui.setupUi(self)

class CountryForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dr = DaterForm()
    dr.show()

    sys.exit(app.exec_())












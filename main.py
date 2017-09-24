# coding: utf-8

from PyQt4 import QtGui, QtCore
import sys
import os.path
from Country import Ui_Form
from Event import Ui_MainWindow


class ActionForm(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



class CountryForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':


    app = QtGui.QApplication(sys.argv)

    act = ActionForm()
    act.show()

    sys.exit(app.exec_())












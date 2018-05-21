#! /usr/bin/env python
# -*- coding=utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from form import Ui_Form


class myui(QtWidgets.QWidget, Ui_Form):
    def __init__(self):    
        super(myui,self).__init__()    
        self.setupUi(self)

    #定义槽函数
    def hello(self):
        self.textEdit.setText("hello world")


app = QtWidgets.QApplication(sys.argv)
window = myui()
window.show()
sys.exit(app.exec_())

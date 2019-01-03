# -*- coding: utf-8 -*-
'''
@File  : 2_icon.py
@Author: SangYu
@Date  : 2019/1/2 10:31
@Desc  : Show an icon in the titlebar of the window
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        root = QFileInfo(__file__).absolutePath()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon(root+'/images/cat.ico'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
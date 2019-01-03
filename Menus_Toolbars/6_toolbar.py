# -*- coding: utf-8 -*-
'''
@File  : 6_toolbar.py
@Author: SangYu
@Date  : 2019/1/2 13:03
@Desc  : Create a toolbar with exit the application
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        root = QFileInfo(__file__).absolutePath()
        exitAct = QAction(QIcon(root+'/images/quit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('&Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
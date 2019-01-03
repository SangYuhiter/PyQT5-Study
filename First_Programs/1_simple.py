# -*- coding: utf-8 -*-
'''
@File  : 1_simple.py
@Author: SangYu
@Date  : 2019/1/2 10:27
@Desc  : Create a simple window in PyQT5
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
'''
@File  : 3_slider.py
@Author: SangYu
@Date  : 2019/1/3 10:23
@Desc  : Show a QSlider widget
'''

from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('images/mute.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('images/mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('images/sound.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('images/mute.png'))
        else:
            self.label.setPixmap(QPixmap('images/sound.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
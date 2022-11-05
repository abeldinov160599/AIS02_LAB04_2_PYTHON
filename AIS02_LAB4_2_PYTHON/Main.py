#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/ais_image.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear_keywords.clicked.connect(self.clear_keywords)
        self.btn_clear_program.clicked.connect(self.clear_program)

    def solve(self):

        text = self.textEdit_text.toPlainText()  # получаем наш текст
        text2 = self.textEdit_words.toPlainText()
        abzats = []
        for i in range(len(text2)):
            if text2[i] == " ":
                abzats.append(1)
            if text2[i] == "\n":
                abzats.append(1)
        abzats.append(1)
        txt = text.split()
        txt2 = text2.split()
        result = ""

        for i in txt2:
            for j in txt:
                if i == j:
                    word = i.upper()
                    txt2[txt2.index(j)] = word
                    break
        for j in range(len(txt2)):
            if abzats[j] == 0:
                result += txt2[j] + " "
            if abzats[j] == 1:
                result += txt2[j] + "\n"

        self.textEdit_words.setPlainText(result)

    def clear_keywords(self):
        self.textEdit_text.clear()

    def clear_program(self):
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

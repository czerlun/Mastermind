#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import os

class Reguły_Gry():
    def __init__(self):
        self.tab = []
        self.x1 = random.randint(1,6)
        self.tab.append(self.x1)
        self.x2 = random.randint(1,6)
        self.tab.append(self.x2)
        self.x3 = random.randint(1,6)
        self.tab.append(self.x3)
        self.x4 = random.randint(1,6)
        self.tab.append(self.x4)
        self.tura = 0
    
    def PR(self):
        print(self.x1,self.x2,self.x3,self.x4)

class Niepoprawne_odpowiedzi():
    pass


class Logika(Reguły_Gry):
    def __init__(self):
        super().__init__()
        self.xx1 = 0
        self.xx2 = 0
        self.xx3 = 0
        self.xx4 = 0
        self.poprawne = 0
        self.wystepujace = 0

    def Turn(self):
        linia = input()
        self.xx1,self.xx2,self.xx3,self.xx4 = linia.split() 
        self.tura += 1

    def sprawdzenie(self):
        self.poprawne = 0
        self.wystepujace = 0
        print("X,X,X,X")
        if int(self.xx1) == self.x1:
            self.poprawne +=1
        elif int(self.xx1) in self.tab:
            self.wystepujace +=1
        if int(self.xx2) == self.x2:
            self.poprawne +=1
        elif int(self.xx2) in self.tab:
            self.wystepujace +=1
        if int(self.xx3) == self.x3:
            self.poprawne +=1
        elif int(self.xx3) in self.tab:
            self.wystepujace +=1
        if int(self.xx4) == self.x4:
            self.poprawne +=1
        elif int(self.xx4) in self.tab:
            self.wystepujace +=1
        print("Poprawne = ", self.poprawne)
        print("Występują = ", self.wystepujace)
        print("Twój typ : ",self.xx1,self.xx2,self.xx3,self.xx4)
        if self.poprawne == 4:
            print("Wygrana!!!")
            sys.exit()
         
a = Logika()
a.PR()





################################################################################
## Form generated from reading UI file 'designerENWcRn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Mastermind(object):
    def setupUi(self, Mastermind):
        if not Mastermind.objectName():
            Mastermind.setObjectName(u"Mastermind")
        Mastermind.resize(361, 483)
        self.Sprawdz = QPushButton(Mastermind)
        self.Sprawdz.setObjectName(u"Sprawdz")
        self.Sprawdz.setGeometry(QRect(240, 340, 88, 34))
        self.oszust = QPushButton(Mastermind)
        self.oszust.setObjectName(u"oszust")
        self.oszust.setGeometry(QRect(240, 250, 88, 34))
        self.reset = QPushButton(Mastermind)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(240, 300, 88, 34))
        self.x1 = QTextEdit(Mastermind)
        self.x1.setObjectName(u"x1")
        self.x1.setGeometry(QRect(30, 330, 31, 41))
        self.x2 = QTextEdit(Mastermind)
        self.x2.setObjectName(u"x2")
        self.x2.setGeometry(QRect(80, 330, 31, 41))
        self.x4 = QTextEdit(Mastermind)
        self.x4.setObjectName(u"x4")
        self.x4.setGeometry(QRect(180, 330, 31, 41))
        self.x3 = QTextEdit(Mastermind)
        self.x3.setObjectName(u"x3")
        self.x3.setGeometry(QRect(130, 330, 31, 41))
        self.label = QLabel(Mastermind)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(37, 387, 201, 71))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Mastermind)

        QMetaObject.connectSlotsByName(Mastermind)
    # setupUi

    def retranslateUi(self, Mastermind):
        Mastermind.setWindowTitle(QCoreApplication.translate("Mastermind", u"Dialog", None))
        self.Sprawdz.setText(QCoreApplication.translate("Mastermind", u"Sprawdz", None))
        self.oszust.setText(QCoreApplication.translate("Mastermind", u"Oszust!", None))
        self.reset.setText(QCoreApplication.translate("Mastermind", u"Reset", None))
        self.label.setText(QCoreApplication.translate("Mastermind", u"Witam!", None))
    # retranslateUi





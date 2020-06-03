#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import os
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)
from PySide2.QtCore import Slot, Qt

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

class Interface(QWidget):
    def __init__(self, x1,x2,x3,x4):
        QWidget.__init__(self)

        self.button1 = QPushButton("Sprawdz!")
        self.button2 = QPushButton("Oszust!")
        self.button3 = QPushButton("Reset!")
        self.text = QLabel("{}{}{}{}".format(x1,x2,x3,x4))
        self.text.setAlignment(Qt.AlignCenter)
        self.x1 = QLineEdit(self)
        self.x2 = QLineEdit(self)
        self.x3 = QLineEdit(self)
        self.x4 = QLineEdit(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button1.clicked.connect(self.Sprawdz)
        self.button2.clicked.connect(self.Oszust)
        self.button3.clicked.connect(self.Reset)

    @Slot()
    def Sprawdz(self):
        self.text.setText("Sprawdz!")

    def Oszust(self):
        self.text.setText("Oszust!")

    def Reset(self):
        self.text.setText("Reset!")


         
if __name__ == "__main__":

    n = Reguły_Gry()

    app = QApplication(sys.argv)

    widget = Interface(n.x1,n.x2,n.x3,n.x4)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
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

    def Turn(self,a1,a2,a3,a4):
        self.xx1 =a1
        self.xx2 =a2
        self.xx3 =a3
        self.xx4 =a4
        self.tura += 1

    def sprawdzenie(self):
        self.poprawne = 0
        self.wystepujace = 0
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

class Interface(QWidget):
    def __init__(self, rx1,rx2,rx3,rx4):
        QWidget.__init__(self)

        self.button1 = QPushButton("Sprawdz!")
        self.button2 = QPushButton("Oszust!")
        self.button3 = QPushButton("Reset!")
        self.text = QLabel("{}{}{}{}".format(rx1,rx2,rx3,rx4))
        self.poprawne = 0
        self.wystepujace = 0
        self.rx1 = rx1
        self.rx2 = rx2
        self.rx3 = rx3
        self.rx4 = rx4
        self.tura = 1
        self.tab = []
        self.tab.append(rx1)
        self.tab.append(rx2)
        self.tab.append(rx3)
        self.tab.append(rx4)
        self.text.setAlignment(Qt.AlignCenter)
        self.x1 = QLineEdit(self)
        self.x2 = QLineEdit(self)
        self.x3 = QLineEdit(self)
        self.x4 = QLineEdit(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.x1)
        self.layout.addWidget(self.x2)
        self.layout.addWidget(self.x3)
        self.layout.addWidget(self.x4)
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
        self.poprawne=0
        self.wystepujace=0
        tmp_tab = self.tab
        if int(self.rx1) == int(self.x1.text()):
            self.poprawne +=1
            tmp_tab.remove(int(self.x1.text()))
        elif int(self.x1.text()) in tmp_tab:
            self.wystepujace +=1
            tmp_tab.remove(int(self.x1.text()))
        if int(self.rx2) == int(self.x2.text()):
            self.poprawne +=1
            if int(self.x2.text()) in tmp_tab:
                tmp_tab.remove(int(self.x2.text()))
        elif int(self.x2.text()) in tmp_tab:
            self.wystepujace +=1
            tmp_tab.remove(int(self.x2.text()))
        if int(self.rx3) == int(self.x3.text()):
            self.poprawne +=1
            if int(self.x3.text()) in tmp_tab:
                tmp_tab.remove(int(self.x3.text()))
        elif int(self.x3.text()) in tmp_tab:
            self.wystepujace +=1
            tmp_tab.remove(int(self.x3.text()))
        if int(self.rx4) == int(self.x4.text()):
            self.poprawne +=1
            if int(self.x4.text()) in tmp_tab:
                tmp_tab.remove(int(self.x4.text()))
        elif int(self.x4.text()) in tmp_tab:
            self.wystepujace +=1
        
        wynik = "Tura "+str(self.tura)+" : "+ str(self.x1.text()+self.x2.text()+self.x3.text()+self.x4.text()) + " Poprawne ="+str(self.poprawne)+" Wystepujace = "+str(self.wystepujace)
        self.text.setText(self.text.text() + '\n' +wynik)

        if self.x1.text() == str(self.rx1) and self.x2.text() == str(self.rx2) and self.x3.text() == str(self.rx3) and self.x4.text() == str(self.rx4):
            self.text.setText("Wygrana!!!")

        self.x1.clear()
        self.x2.clear()
        self.x3.clear()
        self.x4.clear()
        self.tura +=1


    def Oszust(self):
        self.text.setText("Oszust!")

    def Reset(self):
        self.text.setText("Reset!")


         
if __name__ == "__main__":

    n = Logika()

    app = QApplication(sys.argv)
    widget = Interface(n.x1,n.x2,n.x3,n.x4)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
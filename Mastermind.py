#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import os
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)
from PySide2.QtCore import Slot, Qt

class Interface(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.rand = random.randint(0,10)
        if self.rand > 3:
            self.oszust = 0
        else:
            self.oszust = 1
        self.tura = 1
        self.poprawne = 0
        self.wystepujace = 0
        self.button1 = QPushButton("Sprawdz!")
        self.button2 = QPushButton("Oszust!")
        self.button3 = QPushButton("Reset!")
        self.text = QLabel("Witam!")
        self.text.setAlignment(Qt.AlignCenter)
        self.rx1 = random.randint(1,6)
        self.rx2 = random.randint(1,6)
        self.rx3 = random.randint(1,6)
        self.rx4 = random.randint(1,6)
        self.tab = []
        self.tab.append(self.rx1)
        self.tab.append(self.rx2)
        self.tab.append(self.rx3)
        self.tab.append(self.rx4)
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
        if self.oszust == 0:
            self.button1.clicked.connect(self.Sprawdz)
        else:
            self.button1.clicked.connect(self.Sprawdz2)
        self.button2.clicked.connect(self.Oszust)
        self.button3.clicked.connect(self.Reset)

    @Slot()
    def Sprawdz2(self):
        try:
            a = int(self.x1.text())
            b = int(self.x1.text())
            c = int(self.x1.text())
            d = int(self.x1.text())
        except:
            self.text.setText(self.text.text()+"\nPodaj Dobre Liczby")
        self.poprawne = random.randint(0,4)
        self.wystepujace = random.randint(0,4)
        wynik = "Tura "+str(self.tura)+" : "+ str(self.x1.text()+self.x2.text()+self.x3.text()+self.x4.text()) + " Poprawne ="+str(self.poprawne)+" Wystepujace = "+str(self.wystepujace)
        self.text.setText(self.text.text() + '\n' +wynik)

        if self.x1.text() == str(self.rx1) and self.x2.text() == str(self.rx2) and self.x3.text() == str(self.rx3) and self.x4.text() == str(self.rx4):
            self.text.setText("Wygrana!!!")

        self.x1.clear()
        self.x2.clear()
        self.x3.clear()
        self.x4.clear()
        self.tura +=1

    def Sprawdz(self):
        if self.tura == 12:
            self.text.setText(self.text.text()+ "Porażka , poprawna kombinacja to: " + str(self.rx1)+ str(self.rx2)+ str(self.rx3)+ str(self.rx4))
        else:
            try:
                self.poprawne=0
                self.wystepujace=0
                tmp_tab = self.tab
                if int(self.rx1) == int(self.x1.text()):
                    self.poprawne +=1
                    if int(self.x1.text()) in tmp_tab:
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
            except:
                self.text.setText(self.text.text()+"\nPodaj Dobre Liczby")
        

    def Oszust(self):
        if self.oszust == 1:
            self.text.setText("Złapałeś/łaś mnie!")
        else:
            self.text.setText(self.text.text() + "\nTere fere! " + str(self.rx1)+ str(self.rx2)+ str(self.rx3)+ str(self.rx4))

    def Reset(self):
        self.text.setText("Nowa Gra")
        self.tura = 1
        self.rand = random.randint(0,10)
        if self.rand > 3:
            self.oszust = 0
        else:
            self.oszust = 1
        self.rx1 = random.randint(1,6)
        self.rx2 = random.randint(1,6)
        self.rx3 = random.randint(1,6)
        self.rx4 = random.randint(1,6)

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Interface()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
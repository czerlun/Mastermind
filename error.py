#!/usr/bin/python3
import random
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)
from PySide2.QtCore import Slot, Qt

class Interface(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button1 = QPushButton("Sprawdz!")
        self.button2 = QPushButton("Oszust!")
        self.button3 = QPushButton("Reset!")
        self.text = QLabel("Witam!")
        self.rand = random.randint(0, 10)
        if self.rand > 3:
            self.oszust = 0
            self.button1.clicked.connect(self.Sprawdz)
        else:
            self.oszust = 1
            self.button1.clicked.connect(self.Sprawdz2)
        self.tura = 1
        self.poprawne = 0
        self.wystepujace = 0

        self.text.setAlignment(Qt.AlignCenter)
        self.tab_results = 4*[0]
        for i in range(4):
            self.tab_results[i] = random.randint(1,6)
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
        self.button2.clicked.connect(self.Oszust)
        self.button3.clicked.connect(self.Reset)

    @Slot()
    def Sprawdz2(self):
        try:
            a = int(self.x1.text())
            a = int(self.x1.text())
            a = int(self.x1.text())
            a = int(self.x1.text())
        except:
            self.text.setText(self.text.text()+"\nPodaj Dobre Liczby")
        self.poprawne = random.randint(0, 4)
        self.wystepujace = random.randint(0, 4)
        wynik = "Tura "+str(self.tura)+" : "+ str(self.x1.text()+self.x2.text()+self.x3.text()+self.x4.text()) + " Poprawne ="+str(self.poprawne)+" Wystepujace = "+str(self.wystepujace)
        self.text.setText(self.text.text() + '\n' +wynik)

        if self.x1.text() == str(self.tab_results[0]) and self.x2.text() == str(self.tab_results[1]) and self.x3.text() == str(self.tab_results[2]) and self.x4.text() == str(self.tab_results[3]):
            self.text.setText("Wygrana!!!")

        self.x1.clear()
        self.x2.clear()
        self.x3.clear()
        self.x4.clear()
        self.tura += 1

    def Sprawdz(self):
        rx1 = int(float(self.tab_results[0]))
        rx2 = int(float(self.tab_results[1]))
        rx3 = int(float(self.tab_results[2]))
        rx4 = int(float(self.tab_results[3]))
        if self.tura == 12:
            self.text.setText(self.text.text()+ "Porażka , poprawna kombinacja to: " + str(self.tab_results))
        else:
            self.poprawne=0
            self.wystepujace=0
            tmp_tab = self.tab_results
            if int(rx1) == int(self.x1.text()):
                self.poprawne +=1
                if int(self.x1.text()) in tmp_tab:
                    tmp_tab.remove(int(self.x1.text()))
            elif int(self.x1.text()) in tmp_tab:
                self.wystepujace +=1
                tmp_tab.remove(int(self.x1.text()))
            if int(rx2) == int(self.x2.text()):
                self.poprawne +=1
                if int(self.x2.text()) in tmp_tab:
                    tmp_tab.remove(int(self.x2.text()))
            elif int(self.x2.text()) in tmp_tab:
                self.wystepujace +=1
                tmp_tab.remove(int(self.x2.text()))
            if int(rx3) == int(self.x3.text()):
                self.poprawne +=1
                if int(self.x3.text()) in tmp_tab:
                    tmp_tab.remove(int(self.x3.text()))
            elif int(self.x3.text()) in tmp_tab:
                self.wystepujace +=1
                tmp_tab.remove(int(self.x3.text()))
            if int(rx4) == int(self.x4.text()):
                self.poprawne +=1
                if int(self.x4.text()) in tmp_tab:
                    tmp_tab.remove(int(self.x4.text()))
            elif int(self.x4.text()) in tmp_tab:
                self.wystepujace +=1
            
            wynik = "Tura "+str(self.tura)+" : "+ str(self.x1.text()+self.x2.text()+self.x3.text()+self.x4.text()) + " Poprawne ="+str(self.poprawne)+" Wystepujace = "+str(self.wystepujace)
            self.text.setText(self.text.text() + '\n' +wynik)

            if self.x1.text() == str(rx1) and self.x2.text() == str(rx2) and self.x3.text() == str(rx3) and self.x4.text() == str(rx4):
                self.text.setText("Wygrana!!!")

            self.x1.clear()
            self.x2.clear()
            self.x3.clear()
            self.x4.clear()
            self.tura +=1


    def Oszust(self):
        if self.oszust == 1:
            self.text.setText("Złapałeś/łaś mnie!")
        else:
            self.text.setText(self.text.text() + "\nTere fere! " + str(self.tab_results))

    def Reset(self):
        self.text.setText("Nowa Gra")
        self.tura = 1
        self.rand = random.randint(0, 10)
        if self.rand > 3:
            self.oszust = 0
            self.button1.clicked.connect(self.Sprawdz)
        else:
            self.oszust = 1
            self.button1.clicked.connect(self.Sprawdz2)
        self.tab_results.clear()
        for i in range(4):
            self.tab_results.append(random.randint(1, 6))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Widget = Interface()
    Widget.resize(800, 600)
    Widget.show()
    sys.exit(app.exec_())

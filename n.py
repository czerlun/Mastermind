#!/usr/bin/python3
from random import randint
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit,QSpinBox)
from PySide2.QtCore import Slot, Qt

tab_results = [] 
        
def random_code():
    for _ in range(4):
        tab_results.append(randint(1,6)) 

class Interface(QWidget):

    def Reset(self):
        self.text.setText("Nowa Gra")
        self.tura = 1
        random_code()
        print(tab_results)
        if tab_results[0] >= 2:
            self.oszust_flag=0
        else:
            self.oszust_flag=1

    def __init__(self):
        QWidget.__init__(self)
        button1 = QPushButton("Sprawdz!")
        button2 = QPushButton("Oszust!")
        button3 = QPushButton("Reset!")
        self.text_label = QLabel("Witam!")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.x1 = QSpinBox(self)
        self.x1.setMaximum(6)
        self.x1.setMinimum(1)
        self.x2 = QSpinBox(self)
        self.x2.setMaximum(6)
        self.x2.setMinimum(1)
        self.x3 = QSpinBox(self)
        self.x3.setMaximum(6)
        self.x3.setMinimum(1)
        self.x4 = QSpinBox(self)
        self.x4.setMaximum(6)
        self.x4.setMinimum(1)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.x1)
        self.layout.addWidget(self.x2)
        self.layout.addWidget(self.x3)
        self.layout.addWidget(self.x4)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)
        self.button3.clicked.connect(self.Reset)
        self.tura =1
        self.oszust_flag=0
        random_code()
        print(tab_results)
        if tab_results[0] >= 2:
                oszust_flag=0
        else:
            oszust_flag=1


class RegulyGry():
    def __init__(self,Inter):
        self.poprawna =0
        self.wystepujace =0
        if Inter.oszust_flag == 0:
            Inter.button1.clicked.connect(Logika.Sprawdz)
            Inter.button2.clicked.connect(Logika.Oszust)
        elif Inter.oszust_flag ==1:
            Inter.button1.clicked.connect(Oszust_class.Sprawdz)
            Inter.button2.clicked.connect(Oszust_class.Oszust)


class Oszust_class(RegulyGry):
    def Sprawdz():
        RegulyGry.poprawne = random.randint(0, 3)
        RegulyGry.wystepujace = random.randint(0, 4)
        wynik = "Tura "+str(Interface.tura)+" : "+ str(Interface.x1.value())+str(Interface.x2.value())+str(Interface.x3.value())+str(Interface.x4.value()) + " Poprawne ="+str(poprawne)+" Wystepujace = "+str(wystepujace)
        Interface.text.setText(Interface.text_label.text() + '\n' +wynik)

        if int(Interface.x1.value()) == tab_results[0] and int(Interface.x2.value()) == tab_results[1] and int(Interfacet.x3.value()) == tab_results[2] and int(Interface.x4.value()) == tab_results[3]:
            Interface.text_label.setText("Wygrana!!!")
        RegulyGry.tura += 1

    def Oszust():
        Interface.text_label.setText("Złapałeś/łaś mnie!")

class Logika(RegulyGry):
    def Sprawdz():
        if Inter.tura > 12:
            Inter.text_label.setText(Inter.text_label.text()+ "\nPorażka , poprawna kombinacja to: " + str(tab_results))
        else:
            RegulyGry.poprawne=0
            RegulyGry.wystepujace=0
            tmp_tab = tab_results[:]
    #         if Reg.tab_results[0] == Int.x1.value():
    #             self.poprawne +=1
    #         elif self.x1.value() in tmp_tab:
    #             self.wystepujace +=1
    #             tmp_tab.remove(self.x1.value())
    #         if Reg.tab_results[1] == self.x2.value():
    #             self.poprawne +=1
    #         elif self.x2.value() in tmp_tab:
    #             self.wystepujace +=1
    #             tmp_tab.remove(self.x2.value())
    #         if Reg.tab_results[2] == self.x3.value():
    #             self.poprawne +=1
    #         elif self.x3.value() in tmp_tab:
    #             self.wystepujace +=1
    #             tmp_tab.remove(self.x3.value())
    #         if Reg.tab_results[3] == self.x4.value():
    #             self.poprawne +=1
    #         elif self.x4.value() in tmp_tab:
    #             self.wystepujace +=1
    #             tmp_tab.remove(self.x4.value())
            
    #         wynik = []
    #         wynik.append(str(self.x1.value()))
    #         wynik.append(str(self.x2.value()))
    #         wynik.append(str(self.x3.value()))
    #         wynik.append(str(self.x4.value()))
    #         wynik_w = "".join(wynik)
    #         wynik = str(self.tura)+" : "+wynik_w+" Poprawne ="+str(self.poprawne)+" Wystepujace = "+str(self.wystepujace)
    #         self.text.setText(self.text.text() + '\nTura'+str(self.tura)+ wynik)

    #         if self.x1.value() == self.tab_results[0] and self.x2.value() == self.tab_results[1] and self.x3.value() == self.tab_results[2] and self.x4.value() == self.tab_results[3]:
    #             self.text.setText("Wygrana!!!")
    #         self.tura +=1

    def Oszust(self):
        self.text.setText(self.text.text() + "\nTere fere! " + str(self.tab_results))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Widget = Interface()
    Game = RegulyGry(Widget)
    Widget.resize(800, 600)
    Widget.show()
    sys.exit(app.exec_())

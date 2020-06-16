#!/usr/bin/python3
from random import randint
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit, QSpinBox)
from PySide2.QtCore import Slot, Qt

class Interface(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button1 = QPushButton("Sprawdz!")
        self.button2 = QPushButton("Oszust!")
        self.button3 = QPushButton("Reset!")
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

class RegulyGry():
    def __init__(self, My_interface):
        self.poprawna = 0
        self.wystepujace = 0
        self.oszust_flag = 0
        self.tura = 1
        self.tab_results = []
        for _ in range(4):
            self.tab_results.append(randint(1, 6)) 
        if self.tab_results[0] >= 2:
            self.oszust_flag = 0
        else:
            self.oszust_flag = 1
        self.My_interface = My_interface
        self.My_interface.button3.clicked.connect(self.Reset)

    def Reset(self):
        self.My_interface.text_label.setText("Nowa Gra")
        self.tura = 1
        self.tab_results.clear()
        for _ in range(4):
            self.tab_results.append(randint(1, 6))
        if self.tab_results[0] >= 2:
            self.oszust_flag = 0
        else:
            self.oszust_flag = 1


class Oszust_class(RegulyGry):
    def __init__(self, My_game, My_interface):
        super().__init__(My_interface)
        self.My_game = My_game
        self.My_interface = My_interface
    @Slot()
    def Sprawdz(self):
        self.My_game.poprawne = randint(0, 3)
        self.My_game.wystepujace = randint(0, 4)

        wynik = []
        wynik.append(str(self.My_interface.x1.value()))
        wynik.append(str(self.My_interface.x2.value()))
        wynik.append(str(self.My_interface.x3.value()))
        wynik.append(str(self.My_interface.x4.value()))
        wynik_w = "".join(wynik)

        wynik = str(self.My_game.tura)+" : "+wynik_w+" Poprawne ="+str(self.My_game.poprawne)+" Wystepujace = "+str(self.My_game.wystepujace)
        self.My_interface.text_label.setText(self.My_interface.text_label.text() + '\nTura'+ wynik)

        if self.My_interface.x1.value() == self.My_game.tab_results[0] and self.My_interface.x2.value() == self.My_game.tab_results[1] and self.My_interface.x3.value() == self.My_game.tab_results[2] and self.My_interface.x4.value() == self.My_game.tab_results[3]:
            self.My_interface.text_label.setText("Wygrana!!!")
        self.My_game.tura += 1

    def Oszust(self):
        self.My_interface.text_label.setText("Złapałeś/łaś mnie!")

    def ustaw(self):
        self.My_interface.button1.clicked.connect(self.Sprawdz)
        self.My_interface.button2.clicked.connect(self.Oszust)

class Logika(RegulyGry):
    def __init__(self, My_game, My_interface):
        super().__init__(My_interface)
        self.My_game = My_game
        self.My_interface = My_interface

    @Slot()
    def Sprawdz(self):
        if self.My_game.tura > 12:
            self.My_interface.text_label.setText(self.My_interface.text_label.text()+ "\nPorażka , poprawna kombinacja to: " + str(self.My_game.tab_results))
        else:
            self.My_game.poprawne = 0
            self.My_game.wystepujace = 0
            tmp_tab = self.My_game.tab_results[:]
            if self.My_game.tab_results[0] == self.My_interface.x1.value():
                self.My_game.poprawne += 1
            elif self.My_interface.x1.value() in tmp_tab:
                self.My_game.wystepujace += 1
                tmp_tab.remove(self.My_interface.x1.value())
            if self.My_game.tab_results[1] == self.My_interface.x2.value():
                self.My_game.poprawne += 1
            elif self.My_interface.x2.value() in tmp_tab:
                self.My_game.wystepujace += 1
                tmp_tab.remove(self.My_interface.x2.value())
            if self.My_game.tab_results[2] == self.My_interface.x3.value():
                self.My_game.poprawne += 1
            elif self.My_interface.x3.value() in tmp_tab:
                self.My_game.wystepujace += 1
                tmp_tab.remove(self.My_interface.x3.value())
            if self.My_game.tab_results[3] == self.My_interface.x4.value():
                self.My_game.poprawne += 1
            elif self.My_interface.x4.value() in tmp_tab:
                self.My_game.wystepujace += 1
                tmp_tab.remove(self.My_interface.x4.value())
            
            wynik = []
            wynik.append(str(self.My_interface.x1.value()))
            wynik.append(str(self.My_interface.x2.value()))
            wynik.append(str(self.My_interface.x3.value()))
            wynik.append(str(self.My_interface.x4.value()))
            wynik_w = "".join(wynik)
            wynik = str(self.My_game.tura)+" : "+wynik_w+" Poprawne ="+str(self.My_game.poprawne)+" Wystepujace = "+str(self.My_game.wystepujace)
            self.My_interface.text_label.setText(self.My_interface.text_label.text() + '\nTura'+ wynik)

            if self.My_interface.x1.value() == self.My_game.tab_results[0] and self.My_interface.x2.value() == self.My_game.tab_results[1] and self.My_interface.x3.value() == self.My_game.tab_results[2] and self.My_interface.x4.value() == self.My_game.tab_results[3]:
                self.My_interface.text_label.setText("Wygrana!!!")
            self.My_game.tura += 1

    def Oszust(self):
        self.My_interface.text_label.setText(self.My_interface.text_label.text() + "\nTere fere! " + str(self.My_game.tab_results))


    def ustaw(self):
        self.My_interface.button1.clicked.connect(self.Sprawdz)
        self.My_interface.button2.clicked.connect(self.Oszust)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Widget = Interface()
    Game = RegulyGry(Widget)
    if Game.oszust_flag == 0:
        Wynik = Logika(Game, Widget)
        Wynik.ustaw()
    else:
        Wynik = Oszust_class(Game, Widget)
        Wynik.ustaw()
    Widget.resize(800, 600)
    Widget.show()
    
    sys.exit(app.exec_())

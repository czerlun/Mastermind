#!/usr/bin/python3
import random
import sys
from PySide2.Qtwidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, Qwidget, QLineEdit, QSpinBox)
from PySide2.QtCore import Slot, Qt

TURA = 1

class Interface(Qwidget):
    def __init__(self):
        Qwidget.__init__(self)
        self.button1 = QPushButton("sprawdz!")
        self.button2 = QPushButton("oszust!")
        self.button3 = QPushButton("reset!")
        self.text_label = QLabel("Witam!")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.spin_box = []
        for i in range(4):
            self.spin_box.append(QSpinBox(self))
            self.spin_box[i].setMaximum(6)
            self.spin_box[i].setMinimum(1)
            self.layout.addwidget(self.spin_box[i])
        self.layout = QVBoxLayout()
        self.layout.addwidget(self.text_label)
        self.layout.addwidget(self.button1)
        self.layout.addwidget(self.button2)
        self.layout.addwidget(self.button3)
        self.setLayout(self.layout)

class RegulyGry():
    def __init__(self, my_interface):
        self.poprawna = 0
        self.wystepujace = 0
        self.oszust_flag = False
        self.tab_results = []
        self.tab_user = []
        for _ in range(4):
            self.tab_results.append(random.randint(1, 6)) 
        if self.tab_results[0] >= 2:
            self.oszust_flag = False
        else:
            self.oszust_flag = True
        self.my_interface = my_interface
        self.my_interface.button3.clicked.connect(self.reset)

    def reset(self):
        self.my_interface.text_label.setText("Nowa Gra")
        global TURA 
        TURA = 1
        self.tab_results.clear()
        for _ in range(4):
            self.tab_results.append(random.randint(1, 6))
        if self.tab_results[0] >= 2:
            self.oszust_flag = False
        else:
            self.oszust_flag = True


class oszust_class(RegulyGry):
    def __init__(self, my_game, my_interface):
        super().__init__(my_interface)
        self.my_game = my_game
        self.my_interface = my_interface
    @Slot()
    def sprawdz(self):
        global TURA 
        self.my_game.poprawne = random.randint(0, 3)
        self.my_game.wystepujace = random.randint(0, 4)
        wynik = []
        for i in range(4):
            wynik.append(str(self.my_interface.spin_box[i].value()))
        wynik_w = "".join(wynik)
        wynik = f"{TURA} : {wynik_w} Poprawne = {self.my_game.poprawne} Wystepujace = {self.my_game.wystepujace}"
        self.my_interface.text_label.setText(self.my_interface.text_label.text() + '\nTura'+ wynik)
        TURA =+ 1

    def oszust(self):
        self.my_interface.text_label.setText("Złapałeś/łaś mnie!")

    def ustaw(self):
        self.my_interface.button1.clicked.connect(self.sprawdz)
        self.my_interface.button2.clicked.connect(self.oszust)

class Logika(RegulyGry):
    def __init__(self, my_game, my_interface):
        super().__init__(my_interface)
        self.my_game = my_game
        self.my_interface = my_interface

    @Slot()
    def sprawdz(self):
        global TURA 
        if  TURA > 12:
            self.my_interface.text_label.setText(self.my_interface.text_label.text()+ "\nPorażka , poprawna kombinacja to: " + str(self.my_game.tab_results))
        else:
            self.my_game.poprawne = 0
            self.my_game.wystepujace = 0
            tmp_tab = self.my_game.tab_results[:]
            for i in range(1, 4):
                self.my_game.tab_user.append(self.my_interface.spin_box[i].value())

            if self.my_game.tab_results[0] == self.my_interface.spin_box[0].value():
                self.my_game.poprawne += 1
            elif self.my_interface.spin_box[0].value() in tmp_tab:
                self.my_game.wystepujace += 1
                tmp_tab.remove(self.my_interface.spin_box[0].value())
            if self.my_game.tab_results[1] == self.my_interface.spin_box[1].value():
                self.my_game.poprawne += 1
            elif self.my_interface.spin_box[1].value() in tmp_tab:
                self.my_game.wystepujace += 1
                tmp_tab.remove(self.my_interface.spin_box[1].value())
            if self.my_game.tab_results[2] == self.my_interface.spin_box[2].value():
                self.my_game.poprawne += 1
            elif self.my_interface.spin_box[2].value() in tmp_tab:
                self.my_game.wystepujace += 1
                tmp_tab.remove(self.my_interface.spin_box[2].value())
            if self.my_game.tab_results[3] == self.my_interface.spin_box[3].value():
                self.my_game.poprawne += 1
            elif self.my_interface.spin_box[3].value() in tmp_tab:
                self.my_game.wystepujace += 1
                tmp_tab.remove(self.my_interface.spin_box[3].value())
            
            wynik = []
            for i in range(4):
                wynik.append(str(self.my_interface.spin_box[i].value()))
            wynik_w = "".join(wynik)
            wynik = f"{TURA} : {wynik_w} Poprawne = {self.my_game.poprawne} Wystepujace = {self.my_game.wystepujace}"
            self.my_interface.text_label.setText(self.my_interface.text_label.text() + '\nTura'+ wynik)

            if [[self.spin_box[x].value() for x in self.my_game.tab_user] == self.my_game.tab_results]:
                self.my_interface.text_label.setText("Wygrana!!!")
            #if self.my_interface.spin_box[0].value() == self.my_game.tab_results[0] and self.my_interface.spin_box[1].value() == self.my_game.tab_results[1] and self.my_interface.spin_box[2].value() == self.my_game.tab_results[2] and self.my_interface.spin_box[3].value() == self.my_game.tab_results[3]:
            TURA += 1

    def oszust(self):
        self.my_interface.text_label.setText(self.my_interface.text_label.text() + "\nTere fere! " + str(self.my_game.tab_results))


    def ustaw(self):
        self.my_interface.button1.clicked.connect(self.sprawdz)
        self.my_interface.button2.clicked.connect(self.oszust)

def main():
    app = QApplication(sys.argv)
    widget = Interface()
    game = RegulyGry(widget)
    if game.oszust_flag == False:
        wynik = Logika(game, widget)
    else:
        wynik = oszust_class(game, widget)
    wynik.ustaw()
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

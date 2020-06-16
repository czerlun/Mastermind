#!/usr/bin/python3
import unittest
from random import randint
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit, QSpinBox)
from PySide2.QtCore import Slot, Qt
import Mastermind as master

class ApplicationTest(unittest.TestCase):

    def wynik(self):
        self.inter = master.Interface()
        self.app = master.RegulyGry(self.inter)
        print(self.app.tab_results)

    def trafienia(self):
        self.app.poprawna = 2
        print(self.app.poprawna = 2)

    def tury(self):
        self.app.tura = 12
        self.app.Sprawdz()

    def Oszust(self):
        if self.app.oszust_flag == 1:
            self.app.Oszust()
        elif self.app.oszust_flag ==0:
            self.app.Oszust()

    def reset(self):
        self.app.tura += 10
        self.app.reset()
        self.app.tura += 5
        self.app.Sprawdz()

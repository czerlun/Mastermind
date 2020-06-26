#!/usr/bin/python3
import unittest
import random
import sys
import Mastermind 
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit, QSpinBox)
from PySide2.QtCore import Slot, Qt


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.game = Mastermind.RegulyGry()
        self.example_tab = Mastermind.RegulyGry.tab_user = [1,1,1,1]

    def test_trafienia(self):
        self.good_tab = Mastermind.RegulyGry.tab_results = [1,1,1,1]
        self.assertEqual(self.example_tab, self.good_tab)

    def test_tury(self):
        Mastermind.TURA = 12
        self.game.Sprawdz()

    def test_Oszust(self):
        self.game.oszust_flag = 1
        self.game.Oszust()

    def reset(self):
        Mastermind.TURA = 10
        self.game.reset()
        self.game.tura += 5
        self.game.Sprawdz()


if __name__ == '__main__':
    Widget = Interface()
    Game = RegulyGry(Widget)
    unittest.main()

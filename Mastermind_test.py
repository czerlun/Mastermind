#!/usr/bin/python3
import Mastermind 
import random
import sys
import unittest
from PySide2.QtWidgets import (QApplication, QLabel,QLineEdit, QPushButton,
                               QSpinBox, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.game = Mastermind.RegulyGry()
        self.example_tab = Mastermind.RegulyGry.tab_user = [1, 1, 1, 1]

    def test_trafienia(self):
        self.good_tab = Mastermind.RegulyGry.tab_results = [1, 1, 1, 1]
        self.assertEqual(self.example_tab, self.good_tab)

    def test_tury(self):
        Mastermind.TURA = 14
        self.game.Sprawdz()
        self.assertEqual(f"Porażka , poprawna kombinacja to: {self.my_game.tab_results}", self.my_interface.text_label.text())

    def test_oszust(self):
        self.game.oszust_flag = 1
        self.game.Oszust()
        self.assertEqual("Złapałeś/łaś mnie!", self.my_interface.text_label.text())

    def test_reset(self):
        Mastermind.TURA = 10
        self.game.reset()
        self.game.tura += 5
        self.game.Sprawdz()
        self.assertEqual(1, self.my_game.tura)


if __name__ == '__main__':
    unittest.main()

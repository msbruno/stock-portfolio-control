import unittest
from src.main.main import run
import logging


class MainTest(unittest.TestCase):

    def test_(self):
        path = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio.csv'
        path2 = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio_type.csv'

        result1 = run(path, path2)
        print(result1['ticker'])
        
from src.use_cases.calculate_current_portfolio.calculate_current_portfolio import CalculateCurrentPortfolio
from src.domain.portfolio import Portfolio
import unittest

class CalculateCurrentPortfolioTest(unittest.TestCase):

    def test(self):
        path = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio.csv'
        path2 = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio_type.csv'

        columns = ['data', 'ticker', 'operação', 'qtd', 'pm']
        calculate_current = CalculateCurrentPortfolio(columns, path, path2)
        calculate_current.calculate()

        
from datetime import datetime
from src.external.datatable.pandas_loader import PandasLoader
from src.use_cases.process_operations.process_operations import ProcessOperations
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from test.resources.load_file import path_resource
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolio, MarkPortfolioToMarket
import unittest

def operations():
        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        factory = PandasLoader(DEFAULT_COLUMN_MAPPER_BR)
        data = factory.load(path_operations, path_types)
        process_ops = ProcessOperations(DEFAULT_COLUMN_MAPPER_BR)
        return process_ops.process_operations(data)

class GeneratePortfolioTest(unittest.TestCase):

    def test_generate_portfolio(self):
        generate = GeneratePortfolio(DEFAULT_COLUMN_MAPPER_BR)
        #generate = GeneratePortfolio(MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER_BR), DEFAULT_COLUMN_MAPPER_BR) TODO - Criar teste do yahoo
        data = generate.generate_portfolio(operations(), datetime.strptime("23/09/2021", "%d/%m/%Y"))
        result = to_dict(data, DEFAULT_COLUMN_MAPPER_BR.ticker())
        self.assertEqual(2, result['FB'][DEFAULT_COLUMN_MAPPER_BR.acc_shares()])
        self.assertEqual(1, result['NET'][DEFAULT_COLUMN_MAPPER_BR.acc_shares()])
        
        print(result)
        #market_value_column = DEFAULT_COLUMN_MAPPER_BR.market_value()
       
        #self.assertEqual(691.92, round(result['FB'][market_value_column],2))
        #self.assertEqual(135.67, round(result['NET'][market_value_column],2))

    

class MarkPortfolioToMarketTest(unittest.TestCase):

     def test_mark_to_market(self):
        column_mapper = DEFAULT_COLUMN_MAPPER_BR
        yahoo = MarkToMarketUsingYahoo(column_mapper)
        marker = MarkPortfolioToMarket(yahoo, column_mapper)
        date =  datetime.strptime("23/09/2021", "%d/%m/%Y")
        portfolio = GeneratePortfolio(column_mapper).generate_portfolio(operations(), date)
        data = marker.mark_to_market(portfolio, date)
        market_value_column = column_mapper.market_value()
        result = to_dict(data, DEFAULT_COLUMN_MAPPER_BR.ticker())
        #self.assertEqual(691.92, round(result['FB'][market_value_column],2))
        self.assertEqual(135.67, round(result['NET'][market_value_column],2))


def to_dict(df, index_column:str=None)->dict:
        result = df.copy()
        if index_column is not None:
                result = result.set_index(index_column)
        return result.to_dict('index')
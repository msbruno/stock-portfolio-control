from datetime import datetime
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from test.resources.load_file import path_resource
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
import unittest

class TreatDataframe(unittest.TestCase):

    def test_mark_to_market(self):
        generate = GeneratePortfolioMarkedToMarket(MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER_BR), DEFAULT_COLUMN_MAPPER_BR)
        data = generate.portfolio_marked_to_market(self.operations(), datetime.strptime("23/09/2021", "%d/%m/%Y"))
        result = data.to_dict(DEFAULT_COLUMN_MAPPER_BR.ticker_column())
        print(result)
        market_value_column = DEFAULT_COLUMN_MAPPER_BR.market_value_column()
        self.assertEqual(345.96, round(result['FB'][market_value_column],2))
        self.assertEqual(135.67, round(result['NET'][market_value_column],2))

    def operations(self):
        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        factory = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER_BR)
        return factory.load(path_operations, path_types)

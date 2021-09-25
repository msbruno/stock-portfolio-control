from datetime import datetime
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from test.resources.load_file import path_resource
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
import unittest

class TreatDataframe(unittest.TestCase):

    def test(self):

        
        process_ops = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        dt_loader = FactoryDataTablePandas(row_factory)
        generate = GeneratePortfolioMarkedToMarket(process_ops, dt_loader, MarkToMarketUsingYahoo())
        
        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        generate.load(path_operations, path_types)
        data = generate.portfolio_marked_to_market(datetime.strptime("23/09/2021", "%d/%m/%Y"))
        #data.print()
        result = data.to_dict()
        print(result)
        self.assertEqual(345.96, round(result['FB']['market_value'],2))
        self.assertEqual(135.67, round(result['NET']['market_value'],2))

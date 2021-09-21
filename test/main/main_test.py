from src.external.datatable.datatable_loader import FactoryOperationsDataPandas
from test.resources.load_file import path_resource
from src.domain.portfolio import Portfolio
from src.use_cases.interfaces.datatable import OperationsData
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
import unittest
from src.main.main import run
import logging

path = path_resource('portfolio.csv')
path2 = path_resource('portfolio_type.csv')

class MainTest(unittest.TestCase):

    def test_(self):
        
        
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        loader = FactoryOperationsDataPandas(row_factory)
        df = loader.load(path, path2)

        sut = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        df_result:OperationsData = sut.process_operations(df)
        #df_result.print()
        
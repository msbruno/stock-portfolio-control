from src.external.datatable.mappers import OPERATION_MAPPER
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas, OperationsDataTablePandas
from src.external.use_cases.datatable_loader import FactoryOperationsDataTablePandas
import unittest
from src.main.main import run
import logging


class MainTest(unittest.TestCase):

    def test_(self):
        path = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio.csv'
        path2 = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio_type.csv'

        column_mapper =  ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, column_mapper)
        loader = FactoryOperationsDataTablePandas(row_factory)
        df = loader.load(path, path2)

        sut = ProcessOperations(column_mapper)
        df_result:OperationsDataTablePandas = sut.process_operations(df)
        
        print(df_result.last()._df)
        
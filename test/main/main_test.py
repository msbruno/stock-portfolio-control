from src.domain.portfolio import Portfolio
from src.use_cases.interfaces.datatable import OperationsDataTable
from src.external.datatable.mappers import OPERATION_MAPPER
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas, OperationsDataTablePandas
from src.external.use_cases.datatable_loader import FactoryOperationsDataTablePandas
import unittest
from src.main.main import run
import logging

path = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio.csv'
path2 = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio_type.csv'

class MainTest(unittest.TestCase):

    def test_(self):
        
        column_mapper =  ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, column_mapper)
        loader = FactoryOperationsDataTablePandas(row_factory)
        df = loader.load(path, path2)

        sut = ProcessOperations(column_mapper)
        df_result:OperationsDataTable = sut.process_operations(df)
        df_result.print()
        
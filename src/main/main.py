from src.external.use_cases.datatable_loader import FactoryOperationsDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import OperationsDataTablePandas, FactoryRowDataTablePandas

import pandas_datareader as web
import yfinance as yf
yf.pdr_override()


def run(path:str, path2:str):
   
    pass
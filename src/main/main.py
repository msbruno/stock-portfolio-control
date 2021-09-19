from src.external.use_cases.datatable_loader import DataFrameLoaderPandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import DataFramePandas, FactoryRowDataFramePandas

import pandas_datareader as web
import yfinance as yf
yf.pdr_override()


def run(path:str, path2:str):
    column_mapper =  ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
    loader = DataFrameLoaderPandas(column_mapper)
    df = loader.load(path, path2)

    factory = FactoryRowDataFramePandas(OPERATION_MAPPER, column_mapper)
    pandas_df = DataFramePandas(df, factory)
    sut = ProcessOperations(column_mapper)
    df_result:DataFramePandas = sut.process_operations(pandas_df)

    return df_result._df
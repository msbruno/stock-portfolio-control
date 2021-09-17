
from datetime import datetime
from src.use_cases.portfolio_manager import OperationType
from typing import Iterable
import pandas
from src.use_cases.interfaces.dataframe import DataFrame, DataFrameRow


class DataFrameRowPandas(DataFrameRow):
    def __init__(self, index, data: datetime, ticker:str, operation:str, quantity:int, mean_price:float) -> None:
        self._index = index
        self._data = data
        self._ticker = ticker
        self._quantity = quantity
        self._mean_price = mean_price
        self._operation = operation

    def index(self):
        return self._index

    def data(self):
        return self._data

    def ticker(self):
        return self._ticker

    def shares(self):
        return self._quantity

    def mean_price(self):
        return self._mean_price

    def operation(self):
        return self._operation


DATA_COLUMN = 'data'
TICKER_COLUMN = 'ticker'
OPERATION_COLUMN = 'operação' 
QUANTITY_COLUMN = 'qtd'
MEAN_PRICE_COLUMN = 'pm'

CONVERSOR_ENUM = {
    'COMPRA': OperationType.BUY,
    'VENDA': OperationType.SELL,
    'SPLIT': OperationType.SPLIT,
    'AGRUPAMENTO': OperationType.REVERSE_SPLIT,
    'SUBSCRICAO': OperationType.SUBSCRIPTION,
    'BONIFICACAO': OperationType.BONUS,
}

class FactoryRowDataFramePandas:

    def create(self, index, row: pandas.Series)-> DataFrameRow:
        return DataFrameRowPandas(index,
            row[DATA_COLUMN],
            row[TICKER_COLUMN],
            CONVERSOR_ENUM[row[OPERATION_COLUMN]],
            row[QUANTITY_COLUMN],
            row[MEAN_PRICE_COLUMN]
        )


class DataFramePandas(DataFrame):
    
    def __init__(self, df: pandas.DataFrame, row_factory: FactoryRowDataFramePandas):
        self._df:pandas.DataFrame = df
        self._row_factory = row_factory
        self._row_iterator:Iterable = None
        self._current_row = None
        self._current_index = None
    
    def __iter__(self):
        return self

    def __next__(self)->DataFrameRow:
        self._current_index, self._current_row = next(self._get_row_iterator())
        return self._row_factory.create(self._current_index, self._current_row)
    
    def _get_row_iterator(self):
        if self._row_iterator is None:
            self._row_iterator = self._df.iterrows()
        return self._row_iterator

    def current_row(self):
        return self.current_row

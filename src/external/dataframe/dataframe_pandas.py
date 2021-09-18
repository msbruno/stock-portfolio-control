
from datetime import datetime
from src.external.dataframe.mappers import ColumnMapper
from typing import Any, Iterable
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

class FactoryRowDataFramePandas:

    def __init__(self, operation_mapper:dict, column_mapper:ColumnMapper) -> None:
        self._operation_mapper = operation_mapper
        self._column_mapper = column_mapper

    def create(self, index, row: pandas.Series)-> DataFrameRow:
        return DataFrameRowPandas(index,
            row[self._column_mapper.data_column()],
            row[self._column_mapper.ticker_column()],
            self._operation_mapper[row[self._column_mapper.operation_column()]],
            row[self._column_mapper.quantity_column()],
            row[self._column_mapper.mean_price_column()]
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

    def update(self, index: Any, column:str, value: Any):
        self._df.loc[index, column] = value

    def copy(self):
        return DataFramePandas(self._df.copy(), self._row_factory)


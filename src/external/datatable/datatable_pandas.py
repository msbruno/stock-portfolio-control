from __future__ import annotations
from datetime import datetime

from pandas.core.frame import DataFrame
from src.use_cases.interfaces.mappers import ColumnMapper
from typing import Any, Iterable, List
import pandas
from src.use_cases.interfaces.datatable import OperationsData, OperationRow


class OperationRowPandas(OperationRow):
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

class FactoryRowDataTablePandas:

    def __init__(self, operation_mapper:dict, column_mapper:ColumnMapper) -> None:
        self._operation_mapper = operation_mapper
        self._column_mapper = column_mapper

    def create(self, index, row: pandas.Series)-> OperationRow:
        return OperationRowPandas(index,
            row[self._column_mapper.date_column()],
            row[self._column_mapper.ticker_column()],
            self._operation_mapper[row[self._column_mapper.operation_column()]],
            row[self._column_mapper.quantity_column()],
            row[self._column_mapper.mean_price_column()],
        )

    def column_mapper(self)->ColumnMapper:
        return self._column_mapper

class OperationsDataPandas(OperationsData):
    
    def __init__(self, df: pandas.DataFrame, row_factory: FactoryRowDataTablePandas):
        self._df:pandas.DataFrame = df
        self._row_factory = row_factory
        self._row_iterator:Iterable = None
        self._current_row = None
        self._current_index = None
    
    def __iter__(self):
        return self

    def __next__(self)->OperationRow:
        self._current_index, self._current_row = next(self._get_row_iterator())
        return self._row_factory.create(self._current_index, self._current_row)
    
    def _get_row_iterator(self):
        if self._row_iterator is None:
            self._row_iterator = self._df.iterrows()
        return self._row_iterator
    
    def __column_mapper(self):
        return self._row_factory.column_mapper()

    def current_row(self):
        return self.current_row

    def update(self, index: Any, column:str, value: Any):
        self._df.loc[index, column] = value

    def copy(self):
        return self.__create_dataframe(self._df)

    def __create_dataframe(self, df_to_copy:DataFrame):
        return OperationsDataPandas(df_to_copy.copy(), self._row_factory)

    def last_positions(self, date_limit:datetime=None):
        date_column = self.__column_mapper().date_column()
        ticker_column = self.__column_mapper().ticker_column()
        acc_shares_column = self.__column_mapper().acc_shares()
        result = self._df.copy()
        
        if date_limit is not None:
            result = result[result[date_column] <= date_limit]
        result = result.groupby(ticker_column).tail(1)
        result = result[result[acc_shares_column]>0]
        return self.__create_dataframe(result)

    
    def get_all_tickes(self)->List:
        ticker_column = self.__column_mapper().ticker_column()
        return self._df[ticker_column].tolist()

    
    def first_date(self)->datetime:
        return self._df.iloc[0][self.__column_mapper().date_column()]

    def print(self):
        return print(self._df)

    


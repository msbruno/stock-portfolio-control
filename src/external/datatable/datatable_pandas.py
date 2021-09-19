
from datetime import datetime

from pandas.core.frame import DataFrame
from src.use_cases.interfaces.mappers import ColumnMapper
from typing import Any, Iterable
import pandas
from src.use_cases.interfaces.datatable import OperationsDataTable, DataTableRow


class DataTableRowPandas(DataTableRow):
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

    def create(self, index, row: pandas.Series)-> DataTableRow:
        return DataTableRowPandas(index,
            row[self._column_mapper.data_column()],
            row[self._column_mapper.ticker_column()],
            self._operation_mapper[row[self._column_mapper.operation_column()]],
            row[self._column_mapper.quantity_column()],
            row[self._column_mapper.mean_price_column()],
        )

    def column_mapper(self)->ColumnMapper:
        return self._column_mapper

class OperationsDataTablePandas(OperationsDataTable):
    
    def __init__(self, df: pandas.DataFrame, row_factory: FactoryRowDataTablePandas):
        self._df:pandas.DataFrame = df
        self._row_factory = row_factory
        self._row_iterator:Iterable = None
        self._current_row = None
        self._current_index = None
    
    def __iter__(self):
        return self

    def __next__(self)->DataTableRow:
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
        return OperationsDataTablePandas(df_to_copy.copy(), self._row_factory)

    def last(self, data:str=None):
        if data is not None:
            pass
        ticker_column = self.__column_mapper().ticker_column()
        acc_shares_column = self.__column_mapper().acc_shares()
        result = self._df.copy()
        result = result.groupby(ticker_column).tail(1)
        result = result[result[acc_shares_column]>0]
        return self.__create_dataframe(result)



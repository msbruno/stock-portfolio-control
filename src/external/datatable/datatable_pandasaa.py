from __future__ import annotations
from datetime import datetime
from numpy import void

from pandas.core.frame import DataFrame
from src.use_cases.interfaces.datatable import DataTable, Row
from typing import Any, Iterable, List
import pandas


class RowPandasa(Row):

    def __init__(self, index, row: pandas.Series):
        self.__index = index
        self.__row:pandas.Series = row

    def __getitem__(self,column:str)->Any:
        if column == 'index':
            return self.__index
        return  self.__row[column]


class DataTablePandasa(DataTable):
    
    def __init__(self, df: pandas.DataFrame):
        self._df:pandas.DataFrame = df
        self._row_iterator:Iterable = None
        self._current_row = None
        self._current_index = None
    
    def __iter__(self):
        return self

    def __next__(self)->Row:
        self._current_index, self._current_row = next(self._get_row_iterator())
        return RowPandas(self._current_index, self._current_row)
    
    def __getitem__(self, column):
         return self._df[column]
    
    def _get_row_iterator(self):
        if self._row_iterator is None:
            self._row_iterator = self._df.iterrows()
        return self._row_iterator
    
    def current_row(self):
        return self.current_row

    def update(self, index: Any, column:str, value: Any):
        self._df.loc[index, column] = value

    def copy(self):
        return self.__create_dataframe(self._df)

    def __create_dataframe(self, df_to_copy:DataFrame):
        return DataTablePandas(df_to_copy.copy())

    def limit_date(self, date_column:str, date_limit:datetime)->DataTable:
        result = self._df.copy()
        if date_limit is not None:
            result = result[result[date_column] <= date_limit]
        return self.__create_dataframe(result) 

    def last_group_by(self, column:str)->DataTable:
        result = self._df.copy()
        result = result.groupby(column).tail(1)
        return self.__create_dataframe(result)

    def greater_than_zero(self, column:str)->DataTable:
        result = self._df.copy()
        result = result[result[column]>0]
        return self.__create_dataframe(result)
    
    def unique(self, column:str)->List:
        return self._df[column].unique().tolist()

    def first(self, column:str)->datetime:
        return self._df.iloc[0][column]

    def print(self)->void:
        return print(self._df)

    def to_dict(self, index_column:str=None)->dict:
        result = self._df.copy()
        if index_column is not None:
            result = result.set_index(index_column)
        return result.to_dict('index')
    
    def to_json(self)->dict:
        return self._df.to_json(orient="index")

    def multiply(self, column_result:str, column1:str, column2:str):
        self._df[column_result] = self._df[column1] * self._df[column2]


    


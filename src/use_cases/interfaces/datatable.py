from __future__ import annotations
import abc
from datetime import datetime
from typing import Any, List

from numpy import void


class DataTable(abc.ABC):

    @abc.abstractmethod
    def __next__(self):
        pass

    @abc.abstractmethod
    def current_row(self):
        pass

    @abc.abstractmethod
    def update(self, index: Any, column:str, value: Any):
        pass

    @abc.abstractmethod
    def copy(self)->DataTable:
        pass
    
    @abc.abstractmethod
    def limit_date(self, date_column:str, date_limit:datetime)->DataTable:
        pass
    
    @abc.abstractmethod
    def last_group_by(self, column:str)->DataTable:
        pass
    
    @abc.abstractmethod
    def greater_than_zero(self, column:str)->DataTable:
        pass
    
    @abc.abstractmethod
    def unique(self, column:str)->List:
       pass
    
    @abc.abstractmethod
    def first(self, column:str)->DataTable:
        pass

    @abc.abstractmethod
    def print(self)->void:
        pass
    
    @abc.abstractmethod
    def to_dict(self, index_column:str)->dict:
        pass

    @abc.abstractmethod
    def to_json(self)->dict:
        pass

   

class Row(abc.ABC):

    abc.abstractmethod
    def __getitem__(self,column:str)->Any:
        pass


class DataTableLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str)-> DataTable:
        pass
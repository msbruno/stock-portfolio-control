from __future__ import annotations
import abc
from datetime import date, datetime
from typing import Any

from pandas.core.frame import DataFrame

class OperationsDataTable(abc.ABC):

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
    def copy(self)->OperationsDataTable:
        pass

    @abc.abstractmethod
    def get_all_tickes(self)->list:
        pass

    @abc.abstractmethod
    def first_date(self)->datetime:
        pass

    @abc.abstractmethod
    def last_positions(self, date_limit:datetime)-> OperationsDataTable:
        pass
   

class DataTableRow(abc.ABC):

    @abc.abstractmethod
    def index(self):
        pass

    @abc.abstractmethod
    def data(self):
        pass
    
    @abc.abstractmethod
    def ticker(self):
        pass

    @abc.abstractmethod
    def shares(self):
        pass
    
    @abc.abstractmethod
    def mean_price(self):
        pass

    @abc.abstractmethod
    def operation(self):
        pass
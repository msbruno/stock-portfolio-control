from __future__ import annotations
import abc
from datetime import date, datetime
from typing import Any
from numpy import void
from dataclasses import dataclass
from pandas.core.frame import DataFrame


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
    def get_all_tickes(self)->list:
        pass

    @abc.abstractmethod
    def first_date(self)->datetime:
        pass

    @abc.abstractmethod
    def last_positions(self, date_limit:datetime)-> DataTable:
        pass

    @abc.abstractmethod
    def print(self)->void:
        pass

    @abc.abstractmethod
    def to_dict(self)->dict:
        pass

   
@dataclass
class OperationRow(abc.ABC):
    index:Any
    data: datetime
    ticker: str
    shares: int
    mean_price: float
    operation: str
    fees:float


class DataTableLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str)-> DataTable:
        pass
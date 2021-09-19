from __future__ import annotations
import abc
from typing import Any

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
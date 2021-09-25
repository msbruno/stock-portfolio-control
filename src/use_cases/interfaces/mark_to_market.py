import abc
from datetime import datetime
from src.use_cases.interfaces.datatable import DataTable


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def mark_to_market(self, dt: DataTable,date:datetime=None)->DataTable:
        pass
    
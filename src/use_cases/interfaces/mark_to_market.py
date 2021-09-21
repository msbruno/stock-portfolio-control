import abc
from datetime import datetime
from src.use_cases.interfaces.datatable import OperationsData


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def mark_to_market(self, dt: OperationsData,date:datetime=None)->OperationsData:
        pass
    
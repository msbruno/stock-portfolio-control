import abc
from src.use_cases.interfaces.datatable import OperationsData


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def mark(self, dt: OperationsData):
        pass
    
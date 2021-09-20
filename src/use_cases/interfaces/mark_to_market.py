import abc
from src.use_cases.interfaces.datatable import OperationsDataTable


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def mark(self, dt: OperationsDataTable):
        pass
    
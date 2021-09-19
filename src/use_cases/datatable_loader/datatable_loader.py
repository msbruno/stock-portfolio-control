import abc
from src.use_cases.interfaces.datatable import OperationsDataTable

class DataTableLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str)-> OperationsDataTable:
        pass



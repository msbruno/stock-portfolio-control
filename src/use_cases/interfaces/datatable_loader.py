import abc
from src.use_cases.interfaces.datatable import OperationsData

class OperationsDataLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str)-> OperationsData:
        pass



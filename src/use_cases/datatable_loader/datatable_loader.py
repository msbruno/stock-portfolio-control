import abc
from src.use_cases.interfaces.datatable import DataTable

class DataFrameLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str)-> DataTable:
        pass



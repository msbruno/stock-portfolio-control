
import abc

class DataTableLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, path_operations:str, path_types:str):
        pass
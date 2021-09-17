import abc

class DataFrame(abc.ABC):

    @abc.abstractmethod
    def __next__(self):
        pass

    @abc.abstractmethod
    def current_row(self):
        pass
   

class DataFrameRow(abc.ABC):

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
import abc

class DataFrame(abc.ABC):

    @abc.abstractmethod
    def next_row(self):
        pass

    @abc.abstractmethod
    def current_row(self):
        pass
   

class DataFrameRow(abc.ABC):
    @abc.abstractmethod
    def data(self):
        pass
    
    @abc.abstractmethod
    def ticker(self):
        pass

    @abc.abstractmethod
    def quantity(self):
        pass
    
    @abc.abstractmethod
    def mean_price(self):
        pass

    @abc.abstractmethod
    def operation(self):
        pass

import abc
from src.domain.asset import Asset


    
'''def sell(self, operation: OperationData)-> OperationProfit:

    if operation.quantity() > self.__quantity:
        raise Exception("You are trying to sell more {} than you have.".format(self.ticker()))
    operation_profit = OperationProfit(self.mean_price(), operation)
    self.__profit += operation_profit.value()
    self.__quantity -= operation.quantity() 
    self.__value = self.quantity() * self.mean_price()
    return operation_profit
    
def buy(self, operation: OperationData):
    self.__quantity += operation.quantity()
    self.__value += operation.volume()
    self.__mean_price = self.__value / self.__quantity
    return self.__no_operation_profit()
    
def split(self, operation: OperationData):
    self.__quantity = self.__quantity * operation.quantity()
    self.__mean_price = self.__value / self.__quantity
    return self.__no_operation_profit()'''

from enum import Enum

class OperationProfit(abc.ABC):
    @abc.abstractmethod
    def value(self):
        pass

class SellOperationProfit(OperationProfit):

    def __init__(self, asset:Asset, shares:int=0, mean_price:float =0):
        self._asset:Asset = asset
        self._shares = shares
        self._mean_price = mean_price
    
    def value(self):
        if self._shares == 0:
            return 0
        return (self._mean_price - self._asset.mean_price()) * self._shares


class Operation(metaclass=abc.ABCMeta):

    @abc.abstractmethod 
    def execute_on(self, asset:Asset)->OperationProfit:
        pass

class SellOperation(Operation):

    def __init__(self, shares:int, mean_price:float):
        self._shares = shares
        self._mean_price = mean_price
    
    def execute_on(self, asset:Asset)->SellOperationProfit:
        operation_profit = SellOperationProfit(asset, self._shares, self._mean_price)
        asset.add_profit(operation_profit.value())
        asset.reduce_shares(self._shares) 
        return operation_profit
     

import abc
from src.domain.asset import Asset
    
'''def sell(self, operation: OperationData)-> OperationProfit:

def split(self, operation: OperationData):
    self.__quantity = self.__quantity * operation.quantity()
    self.__mean_price = self.__value / self.__quantity
    return self.__no_operation_profit()'''

class OperationProfit(abc.ABC):
    @abc.abstractmethod
    def value(self):
        pass

class NoOperationProfit(OperationProfit):
    def value(self):
        return 0

class SellOperationProfit(OperationProfit):

    def __init__(self, asset:Asset, shares:int=0, value:float =0):
        self._asset:Asset = asset
        self._shares = shares
        self._value = value
    
    def value(self):
        if self._shares == 0:
            return 0
        return (self._mean_price() - self._asset.mean_price()) * self._shares

    def _mean_price(self):
        return self._value / self._shares

class Operation(metaclass=abc.ABCMeta):

    @abc.abstractmethod 
    def execute_on(self, asset:Asset)->OperationProfit:
        pass

class SellOperation(Operation):

    def __init__(self, shares:int, value:float):
        self._shares = shares
        self._value = value
    
    def execute_on(self, asset:Asset)->SellOperationProfit:
        result = SellOperationProfit(asset, self._shares, self._value)
        asset.add_profit(result.value())
        asset.reduce_value(self.amount_to_reduce(asset))
        asset.reduce_shares(self._shares) 
        return result

    def amount_to_reduce(self, asset):
        return self._shares * asset.mean_price()
     
class BuyOperation(Operation):
    def __init__(self, shares:int, value:float):
        self._shares = shares
        self._value = value
 
    def execute_on(self, asset:Asset)->SellOperationProfit:
        asset.add_shares(self._shares)
        asset.add_value(self._value) 
        return NoOperationProfit()       
    
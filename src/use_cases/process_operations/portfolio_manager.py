from enum import Enum
from src.domain.asset import Asset
from src.domain.operation import BuyOperation, OperationProfit, SellOperation, SplitOperation
from src.domain.portfolio import Portfolio

class OperationType(Enum):
    SELL = 'SELL'
    BUY = 'BUY'
    SPLIT = 'SPLIT'
    REVERSE_SPLIT = 'REVERSE_SPLIT'
    SUBSCRIPTION = 'SUBSCRIPTION'
    BONUS = 'BONUS'

class OperationData:  
    
    def __init__(self, shares:int, mean_price:float, operation:OperationType):
        self._mean_price = mean_price
        self._share = shares
        self._operation = operation
     
    def volume(self)->float:
        return self._mean_price * self._share
    
    def shares(self)->int:
        return self._share

    def mean_price(self)->float:
        return self._mean_price

    def operation(self)->OperationType: 
        return self._operation

BUY_OPERATIONS = [OperationType.BUY, OperationType.SUBSCRIPTION, OperationType.BONUS]
SELL_OPERATION = OperationType.SELL
SPLIT_OPERATION = OperationType.SPLIT


class OperationFactory:

    def make(self, data: OperationData):
        if data.operation() in BUY_OPERATIONS:
            return BuyOperation(data.shares(), data.volume())
        elif data.operation() == SELL_OPERATION:
            return SellOperation(data.shares(), data.volume())
        elif data.operation() == SPLIT_OPERATION:
            return SplitOperation(data.shares)
        raise Exception("Operation not allowed.")


class PortfolioManager:

    def __init__(self, portfolio:Portfolio) -> None:
        self._portfolio = portfolio
        self._operation_factory = OperationFactory()

    def execute_operation(self, ticker:str, operation_data:OperationData)-> OperationProfit:
        asset = self.asset(ticker)
        operation = self._operation_factory.make(operation_data)
        return operation.execute_on(asset)

    def asset(self, ticker)->Asset:
        if not self._portfolio.has(ticker):
            self._portfolio.add(Asset(ticker))
        return self._portfolio.get(ticker)
from enum import Enum
from src.domain.asset import Asset
from src.domain.operation import OperationProfit
from src.domain.portfolio import Portfolio

class OperationType(Enum):
    SELL = 'COMPRA'
    BUY = 'VENDA'
    SPLIT = 'SPLIT'
    SUBSCRIPTION = 'SUBSCRICAO'
    BONUS = 'BONIFICACAO'

class OperationData:  
    
    def __init__(self, shares:int, price:int, operation:OperationType):
        self._mean_price = price
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

class PortfolioManager:

    def __init__(self, portfolio:Portfolio) -> None:
        self.__portfolio = portfolio

    def execute_operation(self, ticker:str, operation_data:OperationData)-> OperationProfit:
        asset = self.asset(ticker)

        if operation_data.operation() in BUY_OPERATIONS:
            operation_profit = asset.buy(operation_data)
        elif operation_data.operation() == SELL_OPERATION:
            operation_profit = asset.sell(operation_data)
        elif operation_data.operation() == SPLIT_OPERATION:
            operation_profit = asset.split(operation_data.shares)
        return operation_profit

    def asset(self, ticker)->Asset:
        if not self.__portfolio.has(ticker):
            self.__portfolio.add(Asset(ticker))
        return self.__portfolio.get(ticker)

class Operation: 
    
    def __init__(self, quantity:int, price:int, ):
        self.__mean_price = price
        self.__quantity = quantity
        self.__volume = self.__mean_price * self.__quantity
    
    def volume(self)->float:
        return self.__volume

    def type(self):
        return self.__operation_type  
    
    def quantity(self)->int:
        return self.__quantity

    def mean_price(self)->float:
        return self.__mean_price

class SellOperationProfit:

    def __init__(self, mean_price:float, operation:Operation) -> None:
        self.__mean_price = mean_price
        self.__operation = operation
    
    def value(self):
        return (self.__operation.mean_price() - self.__mean_price) * self.__operation.quantity()

class Asset:
    def __init__(self, ticker:str, quantity=0, mean_price =0, ):
        self.__ticker = ticker
        self.__mean_price = mean_price
        self.__quantity = quantity
        self.__value  = self.__mean_price * self.__quantity
        self.__profit = 0
    
    def sell(self, operation: Operation)-> SellOperationProfit:
        
        if operation.quantity() > self.__quantity:
            raise Exception("You are trying to sell more {} than you have.".format(self.ticker()))
        operation_profit = SellOperationProfit(self.mean_price(), operation)
        self.__quantity -= operation.quantity() 
        self.__profit += operation_profit.value()
        self.__value = self.quantity() * self.mean_price()
        return operation_profit
        
    def buy(self, operation: Operation):
        self.__quantity += operation.quantity()
        self.__value += operation.quantity() * operation.mean_price()
        self.__mean_price = self.__value / self.__quantity
        
    def split(self, split_amount):
        self.__quantity = self.__quantity * split_amount
        self.__mean_price = self.__value / self.__quantity

    def ticker(self)->str:
        return self.__ticker

    def mean_price(self)->float:
        return self.__mean_price

    def quantity(self)->int:
        return self.__quantity
    
    def profit(self)->float:
        return self.__profit

class Portfolio:
    def __init__(self):
        self.assets: dict = {}
    
    def add(self, asset: Asset):
        self.assets[asset.ticker()] = asset
    
    def has(self, ticker:str):
        return ticker in self.assets

     
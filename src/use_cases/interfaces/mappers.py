from src.use_cases.process_operations.portfolio_manager import OperationType


class ColumnMapper:

    def __init__(self, 
    date:str='date', 
    ticker:str='ticker', 
    operation:str='operation', 
    quantity:str='quantity', 
    mean_price:str='mean_price', 
    fees:str='fees',
    currency:str='currency',
    market_value:str='market_value') -> None:
        self.__data = date
        self.__ticker = ticker
        self.__operation = operation
        self.__quantity = quantity
        self.__mean_price = mean_price
        self.__fees = fees
        self.__currency = currency
        self.__market_value = market_value

    def date(self):
        return self.__data

    def ticker(self):
        return self.__ticker

    def operation(self):
        return self.__operation

    def quantity(self):
        return self.__quantity

    def mean_price(self):
        return self.__mean_price

    def fees(self):
        return self.__fees
    
    def op_profit(self):
        return 'profit'
    
    def acc_value(self):
        return 'acc value'
    
    def acc_shares(self):
        return 'acc shares'
    
    def acc_mean_price(self):
        return 'acc mean_price'

    def acc_profit(self):
        return 'acc profit'

    def currency(self):
        return self.__currency
    
    def market_value(self):
        return self.__market_value

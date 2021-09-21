from src.use_cases.process_operations.portfolio_manager import OperationType


class ColumnMapper:

    def __init__(self, 
    date:str='date', 
    ticker:str='ticker', 
    operation:str='operation', 
    quantity:str='quantity', 
    mean_price:str='mean_price', 
    fees:str='fees') -> None:
        self.__data = date
        self.__ticker = ticker
        self.__operation = operation
        self.__quantity = quantity
        self.__mean_price = mean_price
        self.__fees = fees

    def date_column(self):
        return self.__data

    def ticker_column(self):
        return self.__ticker

    def operation_column(self):
        return self.__operation

    def quantity_column(self):
        return self.__quantity

    def mean_price_column(self):
        return self.__mean_price

    def fees_column(self):
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

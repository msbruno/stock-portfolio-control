from src.use_cases.process_operations.portfolio_manager import OperationData 


class ResultEntry:

    def __init__(self, buy_operation:OperationData, sell_operation:OperationData):
        self.__buy_operation = buy_operation
        self.__sell_operation = sell_operation
        self.__position_type = ""

    def delta_value(self)->float:
        return self.__buy_operation.volume() - self.__sell_operation.volume() 
    
    def delta_quantity(self)->int:
        return self.__buy_operation.shares() - self.__sell_operation.shares()

    def mean_price(self)->float:
        result = 0
        if (self.delta_quantity() != 0):
            result = self.delta_value() / self.delta_quantity()
        return result
from src.domain.operation import Operation


class ResultEntry:

    def __init__(self, buy_operation:Operation, sell_operation:Operation):
        self.__buy_operation = buy_operation
        self.__sell_operation = sell_operation
        self.__position_type = ""

    def delta_value(self)->float:
        return self.__buy_operation.volume() - self.__sell_operation.volume() 
    
    def delta_quantity(self)->int:
        return self.__buy_operation.quantity() - self.__sell_operation.quantity()

    def mean_price(self)->float:
        result = 0
        if (self.delta_quantity() != 0):
            result = self.delta_value() / self.delta_quantity()
        return result
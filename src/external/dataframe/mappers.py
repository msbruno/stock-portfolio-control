class ColumnPositionMapper():
    def __init__(self, 
        position_column_data:int, 
        position_column_ticker:int, 
        position_column_operation:int, 
        position_column_quantity:int, 
        position_column_mean_price:int) -> None:

        self._position_column_data = position_column_data
        self._position_column_ticker = position_column_ticker
        self._position_column_operation = position_column_operation
        self._position_column_quantity = position_column_quantity
        self._position_column_mean_price = position_column_mean_price

    def data(self):
        return self._position_column_data

    def ticker(self):
        return self._position_column_ticker
    
    def operation(self):
        return self._position_column_operation
    
    def quantity(self):
        return self._position_column_quantity

    def mean_price(self):
        return self._position_column_mean_price
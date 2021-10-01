from src.external.datatable.mappers import OPERATION_MAPPER
from typing import Any
from src.use_cases.interfaces.datatable import Row, DataTable
from src.use_cases.interfaces.mappers import ColumnMapper
from src.domain.asset import Asset
from src.domain.portfolio import Portfolio
from src.use_cases.process_operations.portfolio_manager import OperationData, PortfolioManager

class ProcessOperations:

    def __init__(self, column_mapper:ColumnMapper):
        self.__portfolio_mg :PortfolioManager = PortfolioManager(Portfolio())
        self.__column_mapper = column_mapper
        self.__operation_mapper = OPERATION_MAPPER

    def process_operations(self, df:DataTable)->DataTable:
        self.__df:DataTable = df
        for row in self.__df:
            self._current_row:Row = row
            operation = self.__current_operation()
            profit = self.__portfolio_mg.execute_operation(row[self.__column_mapper.ticker_column()], operation)
            self.__update_dataframe(self._current_row['index'], profit.value())
        return self.df()

    def df(self):
        return self.__df.copy()
    
    def portfolio_mg(self):
        return self.__portfolio_mg

    def _current_asset(self)-> Asset:
        return self.__portfolio_mg.asset(self._current_row[self.__column_mapper.ticker_column()])
    
    def __current_operation(self)-> OperationData:
        row = self._current_row
        shares = self.__column_mapper.quantity_column()
        mean_price = self.__column_mapper.mean_price_column()
        operation =  self.__column_mapper.operation_column()
        fees = self.__column_mapper.fees_column()
        return OperationData(row[shares], row[mean_price], self.__operation_mapper[row[operation]], row[fees])

    def __update_dataframe(self, index:Any, profit:float):
        self.__df.update(index, self.__column_mapper.op_profit(), profit)
        self.__df.update(index, self.__column_mapper.acc_value(), self._current_asset().value())
        self.__df.update(index, self.__column_mapper.acc_shares(), self._current_asset().shares())
        self.__df.update(index, self.__column_mapper.acc_mean_price(), self._current_asset().mean_price())
        self.__df.update(index, self.__column_mapper.acc_profit(), self._current_asset().profit())
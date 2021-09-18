from typing import Any
from src.use_cases.interfaces.dataframe import DataFrame
from src.domain.asset import Asset
from src.domain.portfolio import Portfolio
from src.use_cases.process_operations.portfolio_manager import OperationData, PortfolioManager

class ProcessOperations:

    def __init__(self):
        self._portfolio_mg :PortfolioManager = PortfolioManager(Portfolio())

    def process_operations(self, df:DataFrame)->DataFrame:
        self._df:DataFrame = df
        for row in self._df:
            self._current_row = row
            operation = self.__current_operation()
            profit = self._portfolio_mg.execute_operation(row.ticker(), operation)
            self.__update_dataframe(row.index(), profit.value())
        return self.df()

    def df(self):
        return self._df.copy()
    
    def portfolio_mg(self):
        return self._portfolio_mg

    def _current_asset(self)-> Asset:
        return self._portfolio_mg.asset(self._current_row.ticker())
    
    def __current_operation(self)-> OperationData:
        row = self._current_row
        return OperationData(row.shares(), row.mean_price(), row.operation())

    def __update_dataframe(self, index:Any, profit:float):
        self._df.update(index, 'lucro', profit)
        self._df.update(index, 'total acumulado', self._current_asset().value())
        self._df.update(index, 'qtd acumulado', self._current_asset().shares())
        self._df.update(index, 'pm acumulado', self._current_asset().mean_price())
        self._df.update(index, 'lucro acumulado', self._current_asset().profit())
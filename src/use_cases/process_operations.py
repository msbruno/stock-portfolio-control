from src.domain.portfolio import Portfolio
from src.frames.dataframe_pandas import DataFramePandas
from src.use_cases.portfolio_manager import OperationData, OperationType, PortfolioManager

class ProcessOperation:

    def __init__(self, df:DataFramePandas) -> None:
        self._df:DataFramePandas = df
        self._portfolio_mg :PortfolioManager = PortfolioManager(Portfolio())

    def process_operations(self):
        for row in self._df:
            self._current_row = row
            operation = self.__current_operation()
            profit_value = self._portfolio_mg.execute_operation(row.ticker(), operation)
            #self._df.update(row, profit_value)

    def df(self):
        return self._df
    
    def portfolio_mg(self):
        return self._portfolio_mg

    def __current_asset(self):
        self._portfolio_mg.asset(self._current_row.ticker())
    
    def __current_operation(self)-> OperationData:
        row = self._current_row
        return OperationData(row.shares(), row.mean_price(), row.operation())

    def __update_table(self, index, profit):
        self._df.loc[index, 'lucro'] = profit
        self._df.loc[index, 'total acumulado'] = self.__current_asset.value()
        self._df.loc[index, 'qtd acumulado'] = self.__current_asset.quantity()
        self._df.loc[index, 'pm acumulado'] = self.__current_asset.mean_price()
        self._df.loc[index, 'lucro acumulado'] = self.__current_asset.profit()
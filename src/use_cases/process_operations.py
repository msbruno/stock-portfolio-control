from src.use_cases.portfolio_manager import OperationData, PortfolioManager
import pandas as pd


class ProcessOperation:

    def __init__(self, df:pd.DataFrame) -> None:
        self._df = df.copy()
        self._portfolio_mg :PortfolioManager = PortfolioManager()

    def process_operations(self):
        for index, row in  self._df.iterrows():
            self._current_row = row
            operation = self.__current_operation()
            profit_value = self._portfolio_mg.execute_operation(row[OPERATION_COLUMN], operation)
            self.__update_table(index, profit_value)

    def df(self):
        return self._df
    
    def portfolio_mg(self):
        return self._portfolio_mg

    def __current_asset(self):
        self._portfolio_mg.asset(self._current_row[TICKER_COLUMN])
    
    def __current_operation(self)-> OperationData:
        return OperationData(self._current_row[QUANTITY_COLUMN], self._current_row[MEAN_PRICE_COLUMN])

    def __update_table(self, index, profit):
        self._df.loc[index, 'lucro'] = profit
        self._df.loc[index, 'total acumulado'] = self.__current_asset.value()
        self._df.loc[index, 'qtd acumulado'] = self.__current_asset.quantity()
        self._df.loc[index, 'pm acumulado'] = self.__current_asset.mean_price()
        self._df.loc[index, 'lucro acumulado'] = self.__current_asset.profit()
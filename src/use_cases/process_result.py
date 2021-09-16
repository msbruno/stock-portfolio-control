from test.domain.operation_test import OperationProfitTest
from src.domain.operation import Asset, OperationData, SellOperationProfit, Portfolio, PortfolioManager
import pandas as pd

OPERATION_COLUMN = 'operação' 
SPLIT_COLUMN = 'split'
TICKER_COLUMN = 'ticker'
QUANTITY_COLUMN = 'qtd'
MEAN_PRICE_COLUMN = 'pm'


class Result:

    def __init__(self, df:pd.DataFrame) -> None:
        self.__df = df.copy()
        self.__portfolio_mg :PortfolioManager = PortfolioManager()

    def process_operations(self):
        for index, row in  self.__df.iterrows():
            self.__current_row = row
            operation = self.__current_operation()
            profit_value = self.__portfolio_mg.execute_operation(row[OPERATION_COLUMN], operation)
            self.__update_table(index, profit_value)

    def __current_asset(self):
        self.__portfolio_mg.asset(self.__current_row[TICKER_COLUMN])
    
    def __current_operation(self)-> OperationData:
        return OperationData(self.__current_row[QUANTITY_COLUMN], self.__current_row[MEAN_PRICE_COLUMN])

    def __update_table(self, index, profit):
        self.__df.loc[index, 'lucro'] = profit
        self.__df.loc[index, 'total acumulado'] = self.__current_asset.value()
        self.__df.loc[index, 'qtd acumulado'] = self.__current_asset.quantity()
        self.__df.loc[index, 'pm acumulado'] = self.__current_asset.mean_price()
        self.__df.loc[index, 'lucro acumulado'] = self.__current_asset.profit()
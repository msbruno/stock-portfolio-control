import abc
from datetime import datetime
import pandas as pd
from src.use_cases.generate_portfolio_market_to_market.mark_to_market import MarkToMarket
from src.use_cases.interfaces.mappers import ColumnMapper


class GeneratePortfolio: 

    def __init__(self, 
    column_mapper: ColumnMapper) -> None:
        self.__column_mapper = column_mapper
 
    def generate_portfolio(self, operations: pd.DataFrame, date_filter:datetime=None)->pd.DataFrame:
        result = operations
        result = self.operations_limited_by_date(result, date_filter)
        result = self.last_operations_each_asset(result)
        return result

    def operations_limited_by_date(self, df: pd.DataFrame, date_limit:datetime):
        result = df
        if date_limit is not None:
            result = result[result[self.__column_mapper.date()] <= date_limit]
        return result

    def last_operations_each_asset(self, df: pd.DataFrame):
        result = df
        result = result.groupby(self.__column_mapper.ticker()).tail(1)
        return result

class MarkPortfolioToMarket:

    def __init__(self, 
        mark_to_market:MarkToMarket, 
        column_mapper: ColumnMapper) -> None:
        self.__mark_to_market:MarkToMarket = mark_to_market
        self.__column_mapper = column_mapper

    def mark_to_market(self, porfolio: pd.DataFrame, date_filter:datetime=None, currency:str=None):
        self.__mark_to_market.load_market_values(porfolio, date_filter)

        for index, row in porfolio.iterrows():
            market_value_per_share = self.__mark_to_market.last_market_value(row[self.__column_mapper.ticker()])
            market_value = market_value_per_share * row[self.__column_mapper.acc_shares()]
            porfolio.at[index, self.__column_mapper.market_value()] = market_value

        return porfolio
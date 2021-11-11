import abc
from datetime import datetime
from src.use_cases.generate_portfolio_market_to_market.mark_to_market import MarkToMarket
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.interfaces.datatable import DataTable 


class GeneratePortfolio: 

    def __init__(self, 
    column_mapper: ColumnMapper) -> None:
        self.__column_mapper = column_mapper
 
    def generate_portfolio(self, operations: DataTable, date_filter:datetime=None)->DataTable:
        operations_limited_by_date = operations.limit_date(self.__column_mapper.date(), date_filter)
        last_operations_each_asset = operations_limited_by_date.last_group_by(self.__column_mapper.ticker())
        result = last_operations_each_asset.copy()
        return result

class MarkPortfolioToMarket:

    def __init__(self, 
        mark_to_market:MarkToMarket, 
        column_mapper: ColumnMapper) -> None:
        self.__mark_to_market:MarkToMarket = mark_to_market
        self.__column_mapper = column_mapper

    def mark_to_market(self, porfolio: DataTable, date_filter:datetime=None, currency:str=None):
        self.__mark_to_market.load_market_values(porfolio, date_filter)

        for row in porfolio:
            market_value_per_share = self.__mark_to_market.last_market_value(row[self.__column_mapper.ticker()])
            market_value = market_value_per_share * row[self.__column_mapper.acc_shares()]
            porfolio.update(row['index'], self.__column_mapper.market_value(), market_value)

        return porfolio
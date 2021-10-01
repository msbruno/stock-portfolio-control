import abc
from datetime import datetime
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER
from src.use_cases.interfaces.mark_to_market import MarkToMarket
from src.use_cases.interfaces.datatable import DataTable


class GeneratePortfolioMarkedToMarket:

    def __init__(self, 
    mark_to_market:MarkToMarket) -> None:
        self.__mark_to_market:MarkToMarket = mark_to_market

    def portfolio_marked_to_market(self, operations_datatable: DataTable, date:datetime=None)->DataTable:
        operations_limited_by_date = operations_datatable.limit_date(DEFAULT_COLUMN_MAPPER.date_column(), date)
        last_operations_each_asset = operations_limited_by_date.last_group_by(DEFAULT_COLUMN_MAPPER.ticker_column())
        self.__mark_to_market.load_market_values(last_operations_each_asset, date)
        result = last_operations_each_asset.copy()

        for row in result:
            market_value_per_share = self.__mark_to_market.last_market_value(row[DEFAULT_COLUMN_MAPPER.ticker_column()])
            market_value = market_value_per_share * row[DEFAULT_COLUMN_MAPPER.quantity_column()]
            result.update(row['index'], "market_value", market_value)
        return result
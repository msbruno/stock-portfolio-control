
from src.use_cases.interfaces.datatable import DataTable
from src.use_cases.interfaces.mappers import ColumnMapper


class ConvertCurrency:

    def __init__(self, column_mapper:ColumnMapper) -> None:
        self.column_mapper = column_mapper

    def convert(self, data_operations: DataTable)->DataTable:
        data_operations.multiply(self.column_mapper.mean_price_column(), 
                                 self.column_mapper.mean_price_column(),
                                 self.column_mapper.currency_conversion_rate_column())
        return data_operations
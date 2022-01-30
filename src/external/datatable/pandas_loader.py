from src.use_cases.datatable_operations.datatable_loader import DataTableLoader
from src.use_cases.interfaces.mappers import ColumnMapper
import pandas as pd

class PandasLoader(DataTableLoader):

    def __init__(self, column_mapper:ColumnMapper, csv_separator:str=';', data_format:str='%d/%m/%Y', ) -> None:
        self.__column_mapper = column_mapper
        self.__csv_separator = csv_separator
        self.__date_format = data_format

    def load(self, path_operations:str, path_types:str)-> pd.DataFrame:
        df_operations_pd = self.__load(path_operations)
        df_types_pd = self.__load(path_types)
        result = pd.merge(df_operations_pd, df_types_pd, how="left", on=self.__column_mapper.ticker())
        result = self.__convert_to_datetime(result)
        result = self.__order_bydata(result)
        return result

    def __order_bydata(self, df_operations_pd):
        return df_operations_pd.sort_values(self.__column_mapper.date())

    def __convert_to_datetime(self, df_operations_pd):
        df_operations_pd[self.__column_mapper.date()] = pd.to_datetime(df_operations_pd[self.__column_mapper.date()], format=self.__date_format)
        return df_operations_pd

    def __load(self, path):
        return pd.read_csv(path, self.__csv_separator)

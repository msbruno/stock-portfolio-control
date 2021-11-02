from src.use_cases.interfaces.mappers import ColumnMapper
from src.external.datatable.datatable_pandas import DataTablePandas
from src.use_cases.interfaces.datatable import DataTable, DataTableLoader
import pandas as pd

class FactoryDataTablePandas(DataTableLoader):

    def __init__(self, column_mapper:ColumnMapper, csv_separator:str=';', data_format:str='%d/%m/%Y', ) -> None:
        self.__column_mapper = column_mapper
        self.__csv_separator = csv_separator
        self.__data_format = data_format

    def wrap(self, dataframe:pd.DataFrame):
        result = self.__convert_to_datetime(dataframe)
        result = self.__order_bydata(result)
        return DataTablePandas(result)

    def load(self, path_operations:str, path_types:str)-> DataTable:
        df_operations_pd = self.__load(path_operations)
        df_types_pd = self.__load(path_types)
        result = pd.merge(df_operations_pd, df_types_pd, how="left", on=self.__column_mapper.ticker())
        result = self.__convert_to_datetime(result)
        result = self.__order_bydata(result)
        return DataTablePandas(result)

    def __order_bydata(self, df_operations_pd):
        return df_operations_pd.sort_values(self.__column_mapper.date())

    def __convert_to_datetime(self, df_operations_pd):
        df_operations_pd[self.__column_mapper.date()] = pd.to_datetime(df_operations_pd[self.__column_mapper.date()], format=self.__data_format)
        return df_operations_pd

    def __load(self, path):
        return pd.read_csv(path, self.__csv_separator)

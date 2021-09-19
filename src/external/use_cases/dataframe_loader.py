from pandas.core.frame import DataFrame
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.dataframe_loader.dataframe_loader import DataFrameLoader
import pandas as pd

class DataFrameLoaderPandas(DataFrameLoader):

    def __init__(self, column_mapper: ColumnMapper, csv_separator:str=';', data_format:str='%d/%m/%Y', ) -> None:
        self.__column_mapper = column_mapper
        self.__csv_separator = csv_separator
        self.__data_format = data_format

    def load(self, path_operations:str, path_types:str):
        df_operations_pd = self.__load(path_operations)
        df_operations_pd = self.__convert_to_datetime(df_operations_pd)
        df_operations_pd = self.__order_bydata(df_operations_pd)
    
        df_types_pd = self.__load(path_types)
        self.__current_df = pd.merge(df_operations_pd, df_types_pd, how="left", on=self.__column_mapper.ticker_column())
        return DataFrame(self.__current_df)

    def __order_bydata(self, df_operations_pd):
        return df_operations_pd.sort_values(self.__column_mapper.data_column())

    def __convert_to_datetime(self, df_operations_pd):
        df_operations_pd[self.__column_mapper.data_column()] = pd.to_datetime(df_operations_pd[self.__column_mapper.data_column()], format=self.__data_format)
        return df_operations_pd

    def __load(self, path):
        return pd.read_csv(path, self.__csv_separator)

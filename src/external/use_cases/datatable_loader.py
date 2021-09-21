from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas, OperationsDataPandas
from src.use_cases.interfaces.datatable import OperationsData
from src.use_cases.interfaces.datatable_loader import OperationsDataLoader
import pandas as pd

class FactoryOperationsDataPandas(OperationsDataLoader):

    def __init__(self, factory_row: FactoryRowDataTablePandas, csv_separator:str=';', data_format:str='%d/%m/%Y', ) -> None:
        self.__factory_row = factory_row
        self.__column_mapper = factory_row.column_mapper()
        self.__csv_separator = csv_separator
        self.__data_format = data_format

    def load(self, path_operations:str, path_types:str)-> OperationsData:
        df_operations_pd = self.__load(path_operations)
        df_operations_pd = self.__convert_to_datetime(df_operations_pd)
        df_operations_pd = self.__order_bydata(df_operations_pd)
        df_types_pd = self.__load(path_types)
        self.__current_df = pd.merge(df_operations_pd, df_types_pd, how="left", on=self.__column_mapper.ticker_column())
        return OperationsDataPandas(self.__current_df, self.__factory_row)

    def __order_bydata(self, df_operations_pd):
        return df_operations_pd.sort_values(self.__column_mapper.date_column())

    def __convert_to_datetime(self, df_operations_pd):
        df_operations_pd[self.__column_mapper.date_column()] = pd.to_datetime(df_operations_pd[self.__column_mapper.date_column()], format=self.__data_format)
        return df_operations_pd

    def __load(self, path):
        return pd.read_csv(path, self.__csv_separator)
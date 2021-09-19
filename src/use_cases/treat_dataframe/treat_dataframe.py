import abc
from src.use_cases.datatable_loader.datatable_loader import DataFrameLoader
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.datatable import DataTable


class GeneratePortfolio:

    def __init__(self, process_operations:ProcessOperations, df_loader: DataFrameLoader) -> None:
        self.__process_operation = process_operations
        self.__df_loader = df_loader

    def treat(self, path_dataframe:str, path_dataframe_types:str):
        self.__df_original:DataTable = self.__df_loader.load(path_dataframe)
        self.__df_types:DataTable = self.__df_loader.load(path_dataframe_types)
        self.__df_treated = self.__df_original.copy()
        self.__df_merger(self.__df_treated,self.__df_types)
        self.__df_treated = self.__process_operation.process_operations(self.__df_treated)
        return self

    def last(self):
        self.__df_treated.last
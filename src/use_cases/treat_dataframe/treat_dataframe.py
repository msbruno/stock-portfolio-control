import abc
from src.use_cases.dataframe_loader.dataframe_loader import DataFrameLoader
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.dataframe import DataFrame


class GeneratePortfolio:

    def __init__(self, process_operations:ProcessOperations, df_loader: DataFrameLoader) -> None:
        self.__process_operation = process_operations
        self.__df_loader = df_loader

    def treat(self, path_dataframe:str, path_dataframe_types:str):
        self.__df_original:DataFrame = self.__df_loader.load(path_dataframe)
        self.__df_types:DataFrame = self.__df_loader.load(path_dataframe_types)
        self.__df_treated = self.__df_original.copy()
        self.__df_merger(self.__df_treated,self.__df_types)
        self.__df_treated = self.__process_operation.process_operations(self.__df_treated)
        return self

    def last(self):
        self.__df_treated.last
from datetime import datetime
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.process_operations.process_operations import ProcessOperations


class CalculateCurrentPortfolio:    

    def __init__(self, columns:ColumnMapper, path_operations:str, path_types:str):
        self.__path_operations:str = path_operations
        self.__path_types:str = path_types
        self.__process_operation = ProcessOperations(columns)
        self.__
        

    def calculate(self, date:str, date_format:str):
        self.__date:str = date
        self.__date_format:str = date_format
        date_filter= datetime.strptime(date, date_format)


        self.__process_operation.process_operations()





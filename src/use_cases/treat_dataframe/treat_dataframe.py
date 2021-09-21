import abc
from src.use_cases.interfaces.mark_to_market import MarkToMarket
from src.use_cases.interfaces.datatable_loader import OperationsDataLoader
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.datatable import OperationsData



class GeneratePortfolio:

    def __init__(self, 
    process_operations:ProcessOperations, 
    df_loader: OperationsDataLoader,
    mark_to_market:MarkToMarket) -> None:
        self.__process_operation = process_operations
        self.__df_loader = df_loader
        self.__mark_to_market = mark_to_market

    def load(self, path_datatable_operations:str, path_datatable_types:str):
        self.__original_datatable:OperationsData = self.__df_loader.load(path_datatable_operations, path_datatable_types)
        self.__datatable_result = self.__process_operation.process_operations(self.__original_datatable)
        return self

    def postions_marked_to_market(self):
        return self.__mark_to_market.mark(self.__datatable_result.last())
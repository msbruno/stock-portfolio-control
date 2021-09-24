

from datetime import datetime
from src.use_cases.interfaces.mark_to_market import MarkToMarket
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.datatable import OperationsData, OperationsDataLoader
import plotly.express as px

class GenerateReportPositions:

    def __init__(self, 
    process_operations:ProcessOperations, 
    df_loader: OperationsDataLoader,
    mark_to_market:MarkToMarket,
    printer) -> None:
        self.__process_operation = process_operations
        self.__df_loader = df_loader
        self.__mark_to_market = mark_to_market
        self.__printer = printer
        
    def generate_report(self, path_datatable_operations:str, path_datatable_types:str, date:datetime):
        self.__original_datatable:OperationsData = self.__df_loader.load(path_datatable_operations, path_datatable_types)
        operations:OperationsData = self.__process_operation.process_operations(self.__original_datatable)
        result:OperationsData = self.__mark_to_market.mark_to_market(operations, date)
        
        

        

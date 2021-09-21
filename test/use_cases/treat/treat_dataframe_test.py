from src.external.datatable.datatable_loader import FactoryOperationsDataPandas
from src.external.datatable.mappers import OPERATION_MAPPER
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.treat_dataframe.treat_dataframe import GeneratePortfolio
import unittest

class TreatDataframe(unittest.TestCase):

    def test(self):

        column_mapper = ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
        process_ops = ProcessOperations(column_mapper)
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER ,column_mapper)
        dt_loader = FactoryOperationsDataPandas(row_factory)
        generate = GeneratePortfolio(process_ops, dt_loader, None)

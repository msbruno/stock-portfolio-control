from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.process_operations.portfolio_manager import OperationType

DEFAULT_COLUMN_MAPPER = ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
 
OPERATION_MAPPER = {
    'COMPRA': OperationType.BUY,
    'VENDA': OperationType.SELL,
    'SPLIT': OperationType.SPLIT,
    'AGRUPAMENTO': OperationType.REVERSE_SPLIT,
    'SUBSCRICAO': OperationType.SUBSCRIPTION,
    'BONIFICACAO': OperationType.BONUS,
}
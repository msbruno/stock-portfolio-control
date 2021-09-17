
from abc import ABC
import abc
from src.use_cases.portfolio_manager import OperationType

COLUMN_MAPPER = {
    'DATA_COLUMN' : 'data',
    'TICKER_COLUMN' : 'ticker',
    'OPERATION_COLUMN' : 'operação',
    'QUANTITY_COLUMN' : 'qtd',
    'MEAN_PRICE_COLUMN' : 'pm'
}

OPERATION_MAPPER = {
    'COMPRA': OperationType.BUY,
    'VENDA': OperationType.SELL,
    'SPLIT': OperationType.SPLIT,
    'AGRUPAMENTO': OperationType.REVERSE_SPLIT,
    'SUBSCRICAO': OperationType.SUBSCRIPTION,
    'BONIFICACAO': OperationType.BONUS,
}
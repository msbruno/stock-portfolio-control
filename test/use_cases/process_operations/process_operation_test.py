from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import OperationsDataTablePandas, FactoryRowDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
import unittest
import pandas as pd

class ProcessOperationTest(unittest.TestCase):

    def test_should_process_buy_operation(self):
        columns = ['data', 'ticker', 'operação', 'qtd', 'pm']
        data = [['10/10/2020', 'NET', 'COMPRA', 5, 100], 
                ['10/10/2020', 'NET', 'COMPRA', 5, 300], 
                ['10/10/2020', 'NET', 'VENDA', 2, 100], 
                ['10/10/2020', 'NET', 'VENDA', 2, 100], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        #TODO remove operation mapper and column mapper
        factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        data_table = OperationsDataTablePandas(df, factory)

        self.sut = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        self.df_result:OperationsDataTablePandas = self.sut.process_operations(data_table)
        self.operations_should_correctly_impact_asset()
        self.dataframe_should_be_uptodate()


    def operations_should_correctly_impact_asset(self):
        asset = self.sut.portfolio_mg()._portfolio.get('NET')
        self.assertEqual('NET', asset.ticker())
        self.assertEqual(6, asset.shares())
        self.assertEqual(200, asset.mean_price())
        self.assertEqual(-400, asset.profit())

    def dataframe_should_be_uptodate(self):
        index=0 
        profit=0 
        acc_value=500 
        acc_shares=5 
        acc_mean_price=acc_value/acc_shares
        acc_profit=0 
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

        index+=1 
        profit=0 
        acc_value+=1500 
        acc_shares+=5 
        acc_mean_price=acc_value/acc_shares
        acc_profit=0 
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

        sell = 2
        sell_price = 100
        index+=1 
        acc_shares-=2 
        acc_value = acc_value - (sell * acc_mean_price) 
        acc_mean_price=acc_value/acc_shares
        profit=(sell_price - acc_mean_price)  * sell  
        acc_profit+=profit
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

    def verify_row_data(self, index, profit, acc_value, acc_shares, acc_mean_price, acc_profit):
        _row = self.df_result._df.iloc[index]
        self.assertEqual(profit,_row[DEFAULT_COLUMN_MAPPER.op_profit()])
        self.assertEqual(acc_value,_row[DEFAULT_COLUMN_MAPPER.acc_value()])
        self.assertEqual(acc_shares,_row[DEFAULT_COLUMN_MAPPER.acc_shares()])
        self.assertEqual(acc_mean_price,_row[DEFAULT_COLUMN_MAPPER.acc_mean_price()])
        self.assertEqual(acc_profit,_row[DEFAULT_COLUMN_MAPPER.acc_profit()])
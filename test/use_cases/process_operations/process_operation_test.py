from pandas._libs.tslibs.timestamps import Timestamp
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import DataTablePandas, FactoryRowDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
import unittest
import pandas as pd

class ProcessOperationTest(unittest.TestCase):

    def test_should_process_buy_operation(self):
        columns = ['data', 'ticker', 'operação', 'qtd', 'pm', 'corretagem']
        data = [['10/10/2020', 'NET', 'COMPRA', 5, 100, 5], #pm=101
                ['10/10/2020', 'NET', 'COMPRA', 5, 300,5], #pm=201
                ['10/10/2020', 'NET', 'VENDA', 2, 100, 2], 
                ['10/10/2020', 'NET', 'VENDA', 2, 100, 2], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        data_table = DataTablePandas(df, factory)

        self.sut = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        self.df_result:DataTablePandas = self.sut.process_operations(data_table)
        self.operations_should_correctly_impact_asset()
        self.dataframe_should_be_uptodate()


    def operations_should_correctly_impact_asset(self):
        asset = self.sut.portfolio_mg()._portfolio.get('NET')
        self.assertEqual('NET', asset.ticker())
        self.assertEqual(6, asset.shares())
        self.assertEqual(201, asset.mean_price())
        self.assertEqual(-400, asset.profit())

    def dataframe_should_be_uptodate(self):
        index=0 
        profit=0 
        acc_value=505 
        acc_shares=5 
        acc_mean_price=acc_value/acc_shares
        acc_profit=0 
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

        index+=1 
        acc_value+=1505 
        acc_shares+=5 
        acc_mean_price=acc_value/acc_shares
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

        shares_sold = 2
        sell_price = 101
        index+=1 
        acc_shares-=shares_sold 
        acc_value = acc_value - (shares_sold * acc_mean_price) 
        acc_mean_price=acc_value/acc_shares
        profit=(sell_price - acc_mean_price)  * shares_sold  
        acc_profit+=profit
        self.verify_row_data(index, profit, acc_value, acc_shares, acc_mean_price, acc_profit)

    def verify_row_data(self, index, profit, acc_value, acc_shares, acc_mean_price, acc_profit):
        _row = self.df_result._df.iloc[index]
        self.assertEqual(profit,_row[DEFAULT_COLUMN_MAPPER.op_profit()])
        self.assertEqual(acc_value,_row[DEFAULT_COLUMN_MAPPER.acc_value()])
        self.assertEqual(acc_shares,_row[DEFAULT_COLUMN_MAPPER.acc_shares()])
        self.assertEqual(acc_mean_price,_row[DEFAULT_COLUMN_MAPPER.acc_mean_price()])
        self.assertEqual(acc_profit,_row[DEFAULT_COLUMN_MAPPER.acc_profit()])
import unittest
import pandas as pd

class DataTablePandasTest(unittest.TestCase):

    def test_should_be_iterable(self):
        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        data = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'BUY', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=data, columns=columns)

        for x in df:
            pass
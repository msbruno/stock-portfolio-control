from src.domain.operation import Operation, Portfolio


class Factory:
    
    def sell(self, row):
        return Operation(row['qtd venda'], row['pm venda'])

    def buy(self, row):
        return Operation(row['qtd compra'], row['pm compra'])

        

class Result:


    def process_operations(self, df):
        portfolio = Portfolio()
        for index, row in df.iterrows():
            ativo = self.asset(row['ticker'], portfolio)
            
            
            operacao_lucro = 0

            if row['operação'] in ['COMPRADA', 'SUBSCRICAO', 'BONIFICACAO']:
                operacao = Factory().buy(row)
                ativo.compra(operacao)
            elif row['operação'] == 'VENDIDA':
                venda = Factory().sell(row)
                ativo.vende(venda)
                operacao_pm = resultado.pm()
                operacao_lucro = (operacao_pm - ativo.pm) * (resultado.delta_quantidade * -1)
                
            elif row['operação'] == 'ZERADA':
                pass        
            elif row['operação'] == 'SPLIT':
                try:
                    ativo.split(row['split'])
                except:
                    print(index, row['data'])
                    
            ativo.lucro += operacao_lucro
            atualiza_tabela(df, ativo, index, operacao_lucro)
        return df
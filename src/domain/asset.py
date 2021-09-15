class Asset:
    def __init__(self, ticker:str, quantity=0, mean_price =0):
        self._ticker = ticker
        self._mean_price = mean_price
        self._shares = quantity
        self._value = self._mean_price * self._shares
        self._profit = 0

    def ticker(self)->str:
        return self._ticker

    def mean_price(self)->float:
        return self._mean_price

    def shares(self)->int:
        return self._shares
    
    def reduce_shares(self, value:int):
        if self._shares < value:
            raise Exception("You are trying to sell more {} than you have.".format(self.ticker()))
        self._shares -= value

    def value(self)->float:
        return self._mean_price * self._shares

    def add_profit(self, value:float):
        self._profit += value

    def profit(self):
        return self._profit
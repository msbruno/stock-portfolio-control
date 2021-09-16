class Asset:
    def __init__(self, ticker:str, quantity:int=0, value:float =0):
        self._ticker:str = ticker
        self._shares:int = quantity
        self._value:float = value
        self._profit:float = 0.0

    def ticker(self)->str:
        return self._ticker

    def mean_price(self)->float:
        return self._value / self._shares

    def shares(self)->int:
        return self._shares
    
    def reduce_shares(self, value:int):
        if self._shares < value:
            raise Exception("You are trying to sell more {} than you have.".format(self.ticker()))
        self._shares -= value

    def _update_value(self, value:float):
        if self._value < value:
            raise Exception("You are trying to sell more {} than you have.".format(self.ticker()))

    def add_shares(self, value:int):
        self._shares += value

    def value(self)->float:
        return self._value

    def add_value(self, value:float)->float:
        self._value += value

    def reduce_value(self, value:float)-> float:
        if self._value < value:
            raise Exception("You are trying to sell more value of {} than you have.".format(self.ticker())) 
        self._value -= value

    def add_profit(self, value:float):
        self._profit += value

    def profit(self):
        return self._profit
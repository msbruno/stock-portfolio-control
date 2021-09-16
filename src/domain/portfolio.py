from src.domain.asset import Asset

class Portfolio:
    def __init__(self):
        self.assets: dict = {}
    
    def add(self, asset: Asset):
        self.assets[asset.ticker()] = asset
    
    def has(self, ticker:str):
        return ticker in self.assets
    
    def get(self, ticker:str):
        return self.assets[ticker] 
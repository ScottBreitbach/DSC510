'''Overriding Method Example'''

class SavingsAcct:
    def __init__(self):
        self.intRate = 2
    def getRate(self):
        return self.intRate

class MoneyMarket(SavingsAcct):
    def getRate(self):
        return self.intRate + 1

savings = SavingsAcct()
market = MoneyMarket()

print(savings.getRate())
print(market.getRate())

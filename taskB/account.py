class Account:
    def __init__(self, initial):
        self._balance = initial


    def deposit(self, amt):
        self._balance += amt
        return


    def withdraw(self, amt):
        self._balance -= amt
        return


    def getbalance(self):
        return self._balance
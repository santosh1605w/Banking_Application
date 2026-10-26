class Account:
    def init(self, account_number, balance = 0.0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

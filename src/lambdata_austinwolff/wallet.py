class Wallet:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

    def __repr__(self):
        return f"<Wallet balance: ${self.balance}>"


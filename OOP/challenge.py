class Bank():

    def __init__(self, balance, owner):
        super().__init__()
        self.balance = balance
        self.owner = owner

    def deposit(self, qty):
        self.balance += qty

    def withdrow(self, qty):
        if qty > self.balance:
            return 0
        else:
            self.balance -= qty
            return self.balance


eduardo = Bank(owner="Eduardo", balance=100)

print(eduardo.balance, eduardo.owner)

eduardo.deposit(100)
print(eduardo.balance, eduardo.owner)
print(eduardo.withdrow(500))
print(eduardo.balance, eduardo.owner)

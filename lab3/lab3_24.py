
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount , "қосылды. Жаңа баланс: " ,self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Қателік: Баланс жеткіліксіз!")
        else:
            self.balance -= amount
            print(amount, " алынды. Жаңа баланс: " , self.balance)
        
owner=input()
balance=int(input())
amount=int(input())
acc = Account(owner, balance)
acc.deposit(amount)
amount=int(input())
acc.withdraw(amount)

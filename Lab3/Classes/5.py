class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance




# Creating an account
acc = Account('John Doe', 100)

# Making several deposits and withdrawals
acc.deposit(50)
print(acc.balance)  # Output: 150

acc.withdraw(70)
print(acc.balance)  # Output: 80

# Trying to overdraw
print(acc.withdraw(90))  # Output: 'Insufficient balance'

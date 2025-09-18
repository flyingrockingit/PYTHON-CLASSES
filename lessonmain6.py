from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner


class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient balance in your account.")

    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest applied: {interest}. New balance: {self._balance}")


class CheckAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
            if self._balance < 0:
                print(f"Warning: You are using your overdraft. Overdraft limit remaining: {self._overdraft_limit + self._balance}")
        else:
            print("Withdrawal exceeds overdraft limit.")


def main():
    print("*** Create Saving Account ***")
    sa = SavingAccount("Alice", 500)
    #sa.deposit(1000)
    #sa.withdraw(200)
    #sa.apply_interest()
    print(f"Final Balance: {sa.get_balance()}")

if __name__ == "__main__":
    main()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrew {amount}. New balance: {self.balance}")
        else:
            print("❌ Insufficient funds!")


class SavingAccount(BankAccount):
    def apply_interest(self, rate=0.02):
        interest = self.balance * rate
        self.balance += interest
        print(f"💰 Interest applied: {interest:.2f}. New balance: {self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"✅ Withdrew {amount}. New balance: {self.balance}")
            if self.balance < 0:
                print(f"⚠️ Using overdraft. Limit remaining: {self.overdraft_limit + self.balance}")
        else:
            print("❌ Withdrawal exceeds overdraft limit.")



print("=== Bank Simulator ===")
name = input("Enter your name: ")

accounts = {
    "saving": SavingAccount(name, 0),
    "checking": CheckingAccount(name, 0)
}

print(f"✅ Accounts created for {name}: Saving and Checking")

while True:
    print("\nChoose account to operate on:")
    print("1. Saving")
    print("2. Checking")
    print("3. Exit")
    acc_choice = input("Enter choice: ").strip()

    if acc_choice == "3":
        print("👋 Goodbye!")
        break
    elif acc_choice == "1":
        account = accounts["saving"]
    elif acc_choice == "2":
        account = accounts["checking"]
    else:
        print("❌ Invalid choice")
        continue

    while True:
        print(f"\n--- {account.owner}'s {type(account).__name__} ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        if isinstance(account, SavingAccount):
            print("4. Apply Interest")
            print("5. Switch Account")
        else:
            print("4. Switch Account")

        op = input("Choose an operation: ").strip()

        if op == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif op == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif op == "3":
            print(f"Balance: {account.balance}")
        elif op == "4" and isinstance(account, SavingAccount):
            account.apply_interest()
        elif (op == "4" and isinstance(account, CheckingAccount)) or \
             (op == "5" and isinstance(account, SavingAccount)):

            break
        else:
            print("❌ Invalid option. Try again.")

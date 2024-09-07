class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_name} Successful")
            print(f"{self.balance} is the remaining balance in {self.account_name} account")
        else:
            print("Invalid amount deposit")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal {amount} from {self.account_name} Successful")
            print(f"{self.balance} is the remaining balance in {self.account_name} account")
        else:
            print("Invalid amount or Insufficient Balance")
    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transfer {amount} to {target_account.account_name}")
            print(f"{self.balance} is the remaining balance in your account")
        else:
            print("Invalid amount deposit")
    def show_balance(self):
        print(f"Account Name: {self.account_name} with Account Number: {self.account_number} has Balance of ${self.balance}")
        

account_1 = BankAccount("8116415084", "Illustrious Code", 0)
account_2 = BankAccount("8033599105", "Noah", 0)
account_3 = BankAccount("08028277421", "Mary", 0)

account_1.deposit(int(input("Enter Amount to Deposit: ")))
account_2.deposit(int(input("Enter Amount to Deposit: ")))
account_3.deposit(int(input("Enter Amount to Deposit: ")))

account_1.withdraw(int(input("Enter Amount to Withdraw: ")))
account_2.withdraw(int(input("Enter Amount to Withdraw: ")))
account_3.withdraw(int(input("Enter Amount to Withdraw: ")))

account_2.transfer(int(input("Enter Amount to Transfer: ")), account_1)
account_1.show_balance()
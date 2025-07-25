
class BankAccount:
    def __init__(self, accountnumber, holder, balance):
        self.accountnumber = accountnumber
        self.holder = holder
        self.balance = balance

    def acinfo(self):
        print(f" Acc_no: {self.accountnumber}")
        print(f" Acc_holder: {self.holder}")
        print(f" Acc_bal: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"After deposit, balance is: {self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" After withdrawal balance is: {self.balance}")
        else:
            print(" Insufficient balance.")


class Saving(BankAccount):
    def __init__(self, ist, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.ist = ist

    def acinfo(self):
        super().acinfo()
        print(f" inteest rate: {self.ist}%")
        interest = (self.ist * self.balance) / 100
        print(f" interest amount: {interest}")
        print(f" balance after interest: {self.balance + interest}")


class Current(BankAccount):
    def __init__(self, credit_limit, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.credit_limit = credit_limit

    def acinfo(self):
        super().acinfo()
        print(f" credit limit: {self.credit_limit}")

    def withdrawal(self, amount):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
            print(f" withdrawal amount: {amount}")
            print(f"after withdrawal, balance is: {self.balance}")
        else:
            print(" withdrawal denied. Exceeds credit limit.")



print(" Welcome to  Bank ")

while True:
    account_type = input("enter account type 1 saving , 2 current  or 3 to quit: ").strip().lower()

    if account_type == "3":
        print(" Thank you for using our bank system!")
        break

    elif account_type == "1":
        try:
            ist = float(input("enter interest rate (%): "))
            acc_num = input("enter account number: ")
            name = input("enter account holder name: ")
            balance = float(input("enter initial balance: "))
            s1 = Saving(ist, acc_num, name, balance)

            while True:
                action = input("do you want to 1 View info, 2 Deposit, 3 Withdraw, 4 Exit this account? Choose 1/2/3/4: ")
                if action == '1':
                    s1.acinfo()
                elif action == '2':
                    amt = float(input("enter amount to deposit: "))
                    s1.deposit(amt)
                elif action == '3':
                    amt = float(input("enter amount to withdraw: "))
                    s1.withdrawal(amt)
                elif action == '4':
                    print(" exiting account session.")
                    break
                else:
                    print(" Invalid please add appropriate input as mentioned ")

        except ValueError:
            print(" Please enter valid numeric values.")

    elif account_type == "2":
        try:
            credit_limit = float(input("enter credit limit: "))
            acc_num = input("enter account number: ")
            name = input("enter account holder name: ")
            balance = float(input("enter initial balance: "))
            c1 = Current(credit_limit, acc_num, name, balance)

            while True:
                action = input(
                    "Do you want to 1 View info, 2 Deposit, 3 Withdraw, 4 Exit this account? Choose 1/2/3/4: ")
                if action == '1':
                    c1.acinfo()
                elif action == '2':
                    amt = float(input("enter amount to deposit: "))
                    c1.deposit(amt)
                elif action == '3':
                    amt = float(input("enter amount to withdraw: "))
                    c1.withdrawal(amt)
                elif action == '4':
                    print("exiting account session.")
                    break
                else:
                    print(" Invalid input. Try again.")

        except ValueError:
            print(" Please enter valid numeric values.")

    else:
        print(" Invalid account type. Please enter 'saving', 'current', or 'exit'.")

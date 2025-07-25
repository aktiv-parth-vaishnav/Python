

class BankAccount:
    def __init__(self, accountnumber, holder, balance):
        self.accountnumber = accountnumber
        self.holder = holder
        self.balance = balance

    def acinfo(self):
        print(f"Account number: {self.accountnumber}")
        print(f"Account holder: {self.holder}")
        print(f"Account balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"After deposit, balance is: {self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"After withdrawal, balance is: {self.balance}")
        else:
            print("Insufficient balance")


class Saving(BankAccount):
    def __init__(self, ist, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.ist = ist

    def acinfo(self):
      super().acinfo()
      print(f"Interest rate: {self.ist}")
      intrest=(self.ist) * (self.balance) / 100
      print(f"ist is: {intrest}")
      print(f"after add ist amout is : {self.balance+intrest} ")


class Current(BankAccount):
    def __init__(self, credit_limit, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.credit_limit = credit_limit


    def acinfo(self):
        super().acinfo()
        print(f"Credit_limit: {self.credit_limit}")

    def withdrawal(self, amount):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
            print(f"withdrwal amoount is {amount} ")
            print(f"After withdrawal, balance is: {self.balance}")
        else:
            print("Withdrawal denied. Exceeds credit_limit limit.")




def is_valid_amount(input_str):
    try:
        value = float(input_str)
        return value > 0
    except ValueError:
        return False


print("Account Creation")
account_type = input("Enter account type (saving/current): ").strip().lower()

if account_type == "saving":
    try:
        ist = float(input("Enter interest rate (%): "))
        acc_num = input("Enter account number: ")
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        s1 = Saving(ist, acc_num, name, balance)
        s1.acinfo()

        deposite = input("Do you want to deposit? (y/n): ").strip().lower()
        if deposite == 'y':
            amount = input("Enter amount to deposit: ")
            if is_valid_amount(amount):
                s1.deposit(float(amount))
            else:
                print("Invalid amount. Deposit must be a positive number.")
        elif deposite == 'n':
            wd_ask = input("Do you want to withdraw? (y/n): ").strip().lower()
            if wd_ask == 'y':
                amount = input("Enter amount to withdraw: ")
                if is_valid_amount(amount):
                    s1.withdrawal(float(amount))
                else:
                    print("Invalid amount. Withdrawal must be a positive number.")
            elif wd_ask == 'n':
                print("Thank you for using our bank.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    except ValueError:
        print("Invalid input! Please enter correct numeric values.")

elif account_type == "current":
    try:
        credit_limit = float(input("Enter credit limit: "))
        acc_num = input("Enter account number: ")
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        c_user = Current(credit_limit, acc_num, name, balance)
        c_user.acinfo()

        deposite = input("Do you want to deposit? (y/n): ").strip().lower()
        if deposite == 'y':
            amount = input("Enter amount to deposit: ")
            if is_valid_amount(amount):
                c_user.deposit(float(amount))
            else:
                print("Invalid amount. Deposit must be a positive number.")
        elif deposite == 'n':
            wd_ask = input("Do you want to withdraw? (y/n): ").strip().lower()
            if wd_ask == 'y':
                amount = input("Enter amount to withdraw: ")
                if is_valid_amount(amount):
                    c_user.withdrawal(float(amount))
                else:
                    print("Invalid amount. Withdrawal must be a positive number.")
            elif wd_ask == 'n':
                print("Thank you for using our bank.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    except ValueError:
        print("Invalid input! Please enter correct numeric values.")

else:
    print("Invalid account type entered. Please enter 'saving' or 'current'.")

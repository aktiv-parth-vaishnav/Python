class BankAccount:
    def __init__(self, accountnumber, holder, balance):
        self.accountnumber = accountnumber
        self.holder = holder
        self.balance = balance

    def acinfo(self):
        print(f"Acc_no: {self.accountnumber}")
        print(f"Acc_holder: {self.holder}")
        print(f"Acc_bal: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"After deposit, balance is: {self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"After withdrawal, balance is: {self.balance}")
        else:
            print("Insufficient balance.")


class Saving(BankAccount):
    def __init__(self, interest_rate, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.interest_rate = interest_rate

    def acinfo(self):
        super().acinfo()
        print(f"Interest rate: {self.interest_rate}%")
        interest = (self.interest_rate * self.balance) / 100
        print(f"Interest amount: {interest}")
        print(f"Balance after interest: {self.balance + interest}")


class Current(BankAccount):
    def __init__(self, credit_limit, accountnumber, holder, balance):
        super().__init__(accountnumber, holder, balance)
        self.credit_limit = credit_limit

    def acinfo(self):
        super().acinfo()
        print(f"Credit limit: {self.credit_limit}")

    def withdrawal(self, amount):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
            print(f"Withdrawal amount: {amount}")
            print(f"After withdrawal, balance is: {self.balance}")
        else:
            print("Withdrawal denied. Exceeds credit limit.")

def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        print(f"Invalid choice! Please select from {choices}.")


# -------- Main Program --------
print("Welcome to the Bank!")

while True:
    account_type = get_choice(
        "Enter account type: 1 Saving, 2 Current, 3 Quit: ",
        ["1", "2", "3"]
    )

    if account_type == "3":
        print("Thank you for using our bank system!")
        break

    acc_num = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = get_float_input("Enter initial balance: ")

    if account_type == "1":
        interest_rate = get_float_input("Enter interest rate (%): ")
        account = Saving(interest_rate, acc_num, name, balance)
    else:
        credit_limit = get_float_input("Enter credit limit: ")
        account = Current(credit_limit, acc_num, name, balance)

    while True:
        action = get_choice(
            "Choose: 1 View info, 2 Deposit, 3 Withdraw, 4 Exit account: ",
            ["1", "2", "3", "4"]
        )

        if action == "1":
            account.acinfo()
        elif action == "2":
            amt = get_float_input("Enter amount to deposit: ")
            account.deposit(amt)
        elif action == "3":
            amt = get_float_input("Enter amount to withdraw: ")
            account.withdrawal(amt)
        elif action == "4":
            print("Exiting account session.")
            break


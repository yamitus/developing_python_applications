class Account:
    def __init__(self):
        self.balance = 0

    def make_deposit(self, deposit):
        self.deposit = deposit
        if self.deposit > 0:
            self.balance = self.balance + self.deposit
        else:
            print("Cannot deposit negative values or 0!")

    def make_withdrawal(self, withdrawal):
        self.withdrawal = withdrawal
        if self.balance > self.withdrawal:
            self.balance = self.balance - self.withdrawal
        else:
            print("Not enough funds!")

    def check_account(self):
        return self.balance

account1 = Account()

def main():
    action = input("What do you want to do? D: Deposit, W: Withdrawal, B: Balance, Q: Quit: ")

    if action == "D" or action == "d":
        amount = int(input("Please set amount to deposit: "))
        account1.make_deposit(amount)
        print("Your balance is:", account1.check_account())
    elif action == "W" or action == "w":
        amount = int(input("Please set the withdrawal amount: "))
        account1.make_withdrawal(amount)
        print("Your account balance is:", account1.check_account())
    elif action == "B" or action == "b":
        print("Your account balance is:", account1.check_account())
    elif action == "Q" or action == "q":
        print("See you!")
        exit()
    else:
        print("That was not an option!")

while True:
    main()
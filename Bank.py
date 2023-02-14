import os
import time
os.system('cls')



class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    def withdraw (self , amount):
        if amount < self.min_withdraw:
            return f"no money for you. Minimum need to take {self.min_withdraw} taka"
        elif amount > self.max_withdraw:
            return f"crosses max limit : {self.max_withdraw}"
        elif amount > self.balance:
            return "No money sorry"
        else:
            self.balance = self.balance -amount5
            return f"Here is yuor money : {amount}"
    def deposit(self, amount):
        self.balance = self.balance + amount


def menu():
    print('Input the bank balance currently you have')
    balance = int(input())
    my_bank = Bank(balance)
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Check Balance')
    print('4. Exit')
    print('Input your choice')
    choice = int(input())
    while 1:
        if choice==1:
            os.system('cls')
            print('Input your withdraw amount')
            withdrawAmount = int(input())
            reply = my_bank.withdraw(withdrawAmount)
            print(reply)
            print('1. Withdraw')
            print('2. Deposit')
            print('3. Check Balance')
            print('4. Exit')
            print('Input your choice')
            choice = int(input())
        elif choice==2:
            os.system('cls')
            print('Input your deposit amount')
            depositAmount = int(input())
            my_bank.deposit(depositAmount)
            print('1. Withdraw')
            print('2. Deposit')
            print('3. Check Balance')
            print('4. Exit')
            print('Input your choice')
            choice = int(input())
        elif choice==3:
            os.system('cls')
            print(f"Current Balance: {my_bank.get_balance()}")
            time.sleep(2)
            print('1. Withdraw')
            print('2. Deposit')
            print('3. Check Balance')
            print('4. Exit')
            print('Input your choice')
            choice = int(input())
        elif choice==4:
            os.system('cls')
            print('\t\t\tThank you')
            break

menu()

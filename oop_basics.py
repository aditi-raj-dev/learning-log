# example 1: mobile phone
class MobilePhone:
    def __init__(self,brand,battery):
        self.brand= brand
        self.battery = battery

    def make_call(self):
        print(self.brand,"is making a call")

    def charge(self):
        self.battery+=10
        print("battery level:",self.battery)

phone= MobilePhone("samsung",50)
phone.make_call()
phone.charge()

# examp-*+le 2 : Bank account

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("deposited",amount)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawn:",amount)
        else:
            print("insufficient balance")

    def show_balance(self):
        print("balance",self.balance)

account=BankAccount("aditi",1000000)
account.deposit(200000)
account.withdraw(50000)
account.show_balance()

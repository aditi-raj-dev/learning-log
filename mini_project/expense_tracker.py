from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.file_name="expenses.txt"
    def add_expenses(self):
        try:
            amount= input("enter amount:")
        except ValueError:
            print(" invalid amount. Please enter a number.")
            return
        note = input ("enter note:")
        date= datetime.now().strftime("%Y-%m-%d")

        with open (self.file_name,"a") as file:
            file.write( f"{date} |{amount} |{note}\n")
            print("expense added successfully.")

    def view_expenses(self):
        try:
            with open (self.file_name,"r")as file:
                expenses=file.readlines()
                if not expenses:
                    print("No expenses recorded.")
                    return
                print("\n -- expenses--")
                for expense in expenses:
                    print(expense.strip())
                
        except FileNotFoundError:
            print("no expenses file found.")

    def total_expense(self):
        total=0
        try:
            with open(self.file_name,"r") as file:
                for line in file:
                    parts = line.split("|")
                    total+=float(parts[1])
            print("total expenses:", total)
        except FileNotFoundError:
            print("no expense to calculate.")
    def menu(self):
        while True:
            print("\n --- expense tracker")
            print("\n1. add expense")
            print("2. view expenses")
            print("3. show total expense")
            print("4. exit")
            choice= input ("enter your choice :")
            if choice =="1":
                self.add_expenses()
            elif choice =="2":
                self.view_expenses()
            elif choice =="2":
                self.total_expenses()
            elif choice=="4":
                print("exiting expense trcker.")
                break
            else:
                print("invalid choice")

if __name__=="__main__":
    tracker=ExpenseTracker()
    tracker.menu()





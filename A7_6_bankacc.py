import sys
class BankAccount:

    def __init__(self,accnum,balance):
        self.accnum=accnum
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Amount has been deposited successfully")

    def withdraw(self,amount):
        if amount>self.balance:
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
            print("Amount has been withdrawed successfully")

    def display(self):
        print(f"Account Number : {self.accnum}\nBalance : {self.balance}")


accnum=input("Enter your account number please: ")
balance=float(input("Enter your balance amount "))
account=BankAccount(accnum,balance)

while(True):
        print("Enter\n1.deposit\n2.withdraw\n3.display\n4.exit")
        choice=int(input())
        
        if choice==1:
             amount=float(input("Enter the amount you want to deposit: "))
             account.deposit(amount)

        elif choice==2:
             amount=float(input("Enter the amount you want to withdraw: "))
             account.withdraw(amount)

        elif choice==3:
             account.display()

        elif choice==4:
             sys.exit(1)
             
        else: 
             print("Invalid choice try again.")
        



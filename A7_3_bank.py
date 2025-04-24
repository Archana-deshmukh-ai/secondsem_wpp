import sys
class bank:
    def __init__(self,accnum,name,balance,acctype):
        self.accnum=accnum
        self.name=name
        self.balance=balance
        self.acctype=acctype

    def deposit(self,amount):
        self.balance+=amount
        print("Amount has been deposited successfully")

    def withdraw(self,amount):
        if amount>self.balance:
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
            print("Amount has been withdrawed successfully")

    def transfer(self,other,amount):
        if(self.balance<amount):
            print("transfer not possible due to insufficient balance ")
        else:
            self.balance-=amount
            other.balance+=amount
            print("Transfer successful")

    def display(self):
        print(f"Account Number : {self.accnum}\n Name : {self.name}\n Balance : {self.balance}\n Account type : {acctype}")


print("Do you want to create an account(type 'yes' or type 'no' if it already exists): ")
c=input().lower()

if(c=='yes'):
    accnum=input("Enter your account number please: ")
    name=input("Enter the name of the customer: ")
    balance=float(input("Enter your balance amount "))
    acctype=input("Enter your account type")
    account=bank(accnum,name,balance,acctype)
else:
    print("No existing account found.Please create an account first.")
    sys.exit(1)

while True:
        
        print("\nEnter\n1.deposit\n2.withdraw\n3.transfer\n4.display\n5.exit")
        choice=int(input())

        if choice==1:
            amount=float(input("Enter the amount you want to deposit: "))
            account.deposit(amount)

        elif choice==2:
            amount=float(input("Enter the amount you want to withdraw: "))
            account.withdraw(amount)

        elif choice==3:
            
            print("Enter the details of the other account: ")
            other_accnum=input("Enter your account number please: ")
            other_name=input("Enter the name of the customer: ")
            other_balance=float(input("Enter your balance amount: "))
            other_acctype=input("Enter your account type: ")
            other_acc=bank(other_accnum,other_name,other_balance,other_acctype)
            amount=float(input("Enter the amount you want to transfer: "))
            account.transfer(other_acc,amount)
            print("Details of the other account: ")
            other_acc.display()

        elif choice==4:
            account.display()

        elif choice==5:
            print("THANK YOU ")
            sys.exit(0)

        else: 
             print("Invalid choice try again.")
        





import sys
class Password_Manager:
    old_password=[]
    def get_password(self):
        return self.old_password[-1]
    def set_password(self,new):
        if new not in self.old_password:
            self.old_password.append(new)
            return 'New password set succesfully'
        else: return 'already exists'
    def is_correct(self,str):
        if str==self.old_password[-1]:
            return True
        else:
            return False
customer=Password_Manager()
print("You have a password manager")
while(True):
    print('''Enter 1.get password\n2.set password\n3.to check the current one\n4.exit\n''')
    choice=int(input("now please enter: "))
    if choice==1:
        cur=customer.get_password()
        print("Your current password is \n\n",cur)
    elif choice==2:
        str=input("Enter your new password")
        print(customer.set_password(str))
    elif choice==3:
        tocheck=input("\nEnter the string to check: ")
        print(customer.is_correct(tocheck))
    elif choice==4:
        sys.exit(1)
    else:
        print("\nInvalid choice, please Enter again ")

        


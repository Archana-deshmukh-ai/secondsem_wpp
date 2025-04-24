class Employee:


    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def __gt__(self,other):
        return self.salary>other.salary
    
    def __lt__(self,other):
        return self.salary<other.salary
    
    def __eq__(self,other):
        return self.salary==other.salary
    


name=input("Enter the name of the Employee 1: ")
salary=float(input("Enter the salary of the Employee 1: "))

e1=Employee(name,salary)

name=input("Enter the name of the Employee 2: ")
salary=float(input("Enter the salary of the Employee 2: "))

e2=Employee(name,salary)

if(e1.salary>e2.salary):
    print(f"\n{e1.name} has higher salary than {e2.name}")

elif(e1.salary<e2.salary):
    print(f"\n{e2.name} has higher salary than {e1.name}")

else:
    print(f"\nBoth {e1.name} and {e2.name} have equal salary ")



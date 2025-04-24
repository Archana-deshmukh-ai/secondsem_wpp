import sys
class node:
    head=None
    
    def __init__(self,data):
        self.data=data
        self.next=None
        

    def push(self,data):
        newnode=node(data)
        if node.head is None:
            node.head=newnode
        else:
            newnode.next=node.head
            node.head=newnode
        print("Data entered successfully.")

    def pop(self):
        if node.head is None:
            print("The stack is empty")
        else:
            temp=node.head
            node.head=node.head.next
            print(f"\n{temp.data} is removed successfully.")
            del(temp)


    def peek(self):
        if node.head is None:
            print("The stack is empty")
        else:
            print(node.head.data)


    def display(self):
        if node.head is None:
            print("The stack is empty")
        else:
            temp=node.head
            print("Stack: ")
            while temp!=None:
                print(f"{temp.data}->",end="")
                temp=temp.next
            print("None")


print("Stack using python.")

stack=node(0)

while True:

    print("Enter 1.push\n2.pop\n3.peek\n4.display\n5.exit")
    choice=int(input())

    if choice==1:
        data=int(input("Enter the data: "))
        stack.push(data)

    elif choice==2:
        stack.pop()

    elif choice==3:
        stack.peek()

    elif choice==4:
        stack.display()

    elif choice==5:
        sys.exit(0)

    else:
        print("INVALID CHOICE,Please try again")
        



    
    


        



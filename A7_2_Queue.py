import sys
class node:
    
    front=None
    rear=None

    def __init__(self,data):
        self.data=data
        self.next=None
    
    def push(self,data):
        
        newnode=node(data)

        if node.front is None and node.rear is None :
            node.front,node.rear=newnode
        else:
            node.rear.next=newnode
            node.rear=newnode
            
        print("Data entered successfully.")

    def pop(self):

        if node.front is None:
            print("The queue is empty")
        else:
            temp=node.front
            node.front=node.front.next

            if node.front is None: 
                node.rear = None #last node

            print(f"\n{temp.data} is removed successfully.")
            del(temp)

    def peek(self):

        if node.front is None:
            print("\nQueue is empty.")
        else:
            print(node.front.data)

    def display(self):
        if node.front is None:
            print("\nQueue is empty.")
        else:
            temp=node.front
            print("queue: ")
            while temp!=None:
                print(f"{temp.data}->",end="")
                temp=temp.next
            print("None")

    print("Queue using python.")

queue=node(0)

while True:

    print("Enter 1.push\n2.pop\n3.peek\n4.display\n5.exit")
    choice=int(input())

    if choice==1:
        data=int(input("Enter the data: "))
        queue.push(data)

    elif choice==2:
        queue.pop()

    elif choice==3:
        queue.peek()

    elif choice==4:
        queue.display()

    elif choice==5:
        print("Exiting program.")
        sys.exit(0)

    else:
        print("INVALID CHOICE,Please try again.")
        







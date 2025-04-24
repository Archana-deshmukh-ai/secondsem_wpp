import math
def squarecheck(num1,num2):
    count=0
    ma=max(num1,num2)
    mi=min(num1,num2)
    for i in range (mi,ma+1):
        j=1
        while j*j<=i:
            if j*j==i:
                count+=1
                print(j*j,end=" ")
            j+=1
    return count
test=int(input("enter the number of test cases: "))
while test!=0:
    num1=int(input("Enter the first number of your choice: "))
    num2=int(input("Enter the second number of your choice: "))
    result=squarecheck(num1,num2) 
    print("\nThe number of perfect squares in between is ",result)
    test-=1
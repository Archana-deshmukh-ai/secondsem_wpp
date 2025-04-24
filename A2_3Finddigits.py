def divide():
    count=0
    digits=0
    num=int(input("Enter the number: "))
    temp=temp1=num
    while num>0:
        digits+=1
        num//=10
    print("The number of digits is ",digits)
    while digits>0:
        rem=temp%10
        if temp1%rem==0:
            count+=1
        digits-=1
    
            
    print("The number is ",count) 


t=int(input("Enter the number of test cases:"))
while t>0:
    divide()
    t-=1
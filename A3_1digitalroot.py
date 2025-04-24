#digit root one 
def sumofdigits(num):
    tempsum=0
    while(num>0):
        rem=num%10
        tempsum+=rem
        num//=10
    return tempsum
    
    
num=int(input("enter the number please: "))
sum=sumofdigits(num)
while sum>9:
    sum=sumofdigits(sum)
print("the digit root is",sum)
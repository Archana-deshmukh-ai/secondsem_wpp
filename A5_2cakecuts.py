#halloween party
def halloween():
    k=int(input("enter the number of times you cut the cake: "))
    if k%2==0:
        cuts=((int(k/2)*int(k/2)))#rows=k/2 and columns=k/2
    else:
        cuts=((int(k/2)*int(k/2+1)))#rows=k/2+1 and columns=k/2
    print("The maximum number of cuts that can be made is ",cuts)

t=int(input("Enter the number of test cases: "))
while t!=0:
    halloween()
    t-=1

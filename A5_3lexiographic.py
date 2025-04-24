#bigger is greater
def nextword():
    result=""
    str=input("Enter the string which you want to convert: ")
    str=str.lower()
    str=list(str)
    l=len(str)
    i=l-2
    while i>=0 and str[i]>=str[i+1]:
        i-=1
    if i==-1:
        print("There is no greater word")
    else:
        j=l-1
        while str[j]<=str[i]:
            j-=1
        str[i],str[j]=str[j],str[i]
        result=str[:i+1] + str[i+1:][::-1]
        final=''.join(str)
    print("The word is ",final)

    
t=int(input("Enter the number of test cases: "))
while t!=0:
    nextword()
    t-=1
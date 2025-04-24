#to capitalise alternate words 
def cap(str):
    
        result=""
        for i,char in enumerate(str):
            if i%2==0:
               result+= char.upper()
            else:
                result+=char
        print(result)
str=input("Enter a word of ur choice: ")

cap(str)


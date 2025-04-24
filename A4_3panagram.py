str=input("Enter the string u want to check: ")
d=dict()
str=str.lower()
for chr in str:
    if 'a' <= chr <= 'z':  
        d[chr] = True  
'''since no duplicate keys are allowed only 26 keys i.e, alphabets can be stored 
if the len of dict is 26 that means that all alphabets are present.'''
if len(d) == 26:
    print("The given string is a pangram.")
else:
    print("The given string is not a pangram.")

    



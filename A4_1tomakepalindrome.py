def min_conversions_to_palindrome(str):
    n=len(str)
    operations=0
    
    for i in range(n//2):
        left_char=str[i]
        right_char=str[n-i-1]
        if left_char!=right_char:
            operations+=abs(ord(left_char)-ord(right_char))
    return operations
test=int(input("Enter the number of test cases:"))
while test!=0:
    input_str=input("Enter the string that you want to check: ")
    checked=min_conversions_to_palindrome(input_str)
    print("The minimum number of operations is ",checked)
    test-=1

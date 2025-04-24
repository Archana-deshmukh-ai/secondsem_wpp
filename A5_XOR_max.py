def maximize_xor(l, r):
   
    max_xor = 0

    for i in range(l, r + 1):
        for j in range(l, r + 1):
            xor_value = i ^ j
            if xor_value > max_xor:
                max_xor = xor_value

    return max_xor

l = int(input("Enter the first number: "))
r = int(input("Enter the second number: "))
if(l<r):
    print(maximize_xor(l, r))  
elif(l<r):
    print(maximize_xor(r,l))
else:
    print("0")

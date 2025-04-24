def utropiantree(num):
    
    height = 1  
    for cycle in range(1, num + 1):
        if cycle % 2 == 1:
            height *= 2  
        else:
            height += 1  
             
    print("The height is ",height)

tes=int(input("Enter the number of test cases: "))
while tes!=0:
       n=int(input("Enter the number of cycles:"))
       utropiantree(n)
       tes-=1







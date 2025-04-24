n=int(input("Enter the number of products"))

dict={}
while n>0:
    p_name=input("Enter the product: ")
    dict[p_name]=int(input("Enter the price of the corresponding product: "))
    n-=1
print("Finished entering the data.\nnow,Enter the product name(-1): ")
take=input()
if take!="-1":
    if take in dict:#you can also write dict.keys(),but it is default
        print("The value is {}".format(dict[take]))
    else:
        print('''"ERROR",given product is not found''')


      





def isfibo( num):
    fib0=0
    fib1=1
    fibn=fib0+fib1
    while (num<fibn):
        fib0=fib1
        fib1=fibn
        fibn=fib0+fib1
    if(num==fibn):
        print("the given number is fibo")
    else:
        print("the given number is not fibo")

t=int(input("Enter the number of test cases please: "))
while t!=0:

    num=int(input("Enter the number you want to test: "))
    test=isfibo(num)
    t-=1

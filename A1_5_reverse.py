while True:
    students=(input(f"Enter student name : "))
    if students==1:
        exit(0)
    print(students[::-1])
#or another method is
#students = [input(f"Enter name of student {i+1}: ") for i in range(15)]
#print("\nReversed names:")
#print(*students[::-1], sep='\n')








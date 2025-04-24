import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])
while(True):
    print("\n\nChoose an option:")
    print("1 - print Original series")
    print("2 - Convert to Uppercase")
    print("3 - Convert to Lowercase")
    print("4 - Find Length of each string")
    print("5 - To exit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice =='1':
        print("\nOriginal : ")
        print(s)

    elif choice == '2':
        print("\nUppercase:")
        print(s.str.upper())

    elif choice == '3':
        print("\nLowercase:")
        print(s.str.lower())

    elif choice == '4':
        print("\nLength of each string:")
        print(s.str.len())
        
    elif choice == '5':
        print("Exiting")
        exit(0)

    else:
        print("\nInvalid choice! Please enter 1, 2, 3, 4, or 5.")

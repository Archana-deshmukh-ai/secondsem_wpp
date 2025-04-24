import pandas as pd
from datetime import datetime, date, time

while(True):
    print("Choose an option:")
    print("1 - Create DateTime object for Jan 15 2012")
    print("2 - Specific date and time of 9:20 PM")
    print("3 - Get Local Date and Time")
    print("4 - Get a Date without Time")
    print("5 - Get Current Date")
    print("6 - Get Time from a DateTime")
    print("7 - Get Current Local Time")
    print("8 - To exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        dt = pd.to_datetime("2012-01-15")
        print("\nDateTime object for Jan 15, 2012:", dt)

    elif choice == 2:
        dt = pd.to_datetime("2023-01-01 21:20")
        print("\nSpecific date and time (9:20 PM):", dt)

    elif choice == 3:
        local_dt = datetime.now()
        print("\nLocal Date and Time:", local_dt)

    elif choice == 4:
        only_date = date.today()
        print("\nDate without time:", only_date)

    elif choice == 5:
        current_date = pd.Timestamp.today().date()
        print("\nCurrent Date:", current_date)

    elif choice == 6:
        sample_datetime = datetime.now()
        print("\nTime from current DateTime:", sample_datetime.time())

    elif choice == 7:
        current_local_time = datetime.now().time()
        print("\nCurrent Local Time:", current_local_time)

    elif choice == 8:
        exit(0)

    else:
        print("\nInvalid choice! Please enter a valid option (1-8).")

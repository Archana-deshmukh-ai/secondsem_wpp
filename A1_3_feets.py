length = float(input("Enter length in feet: "))
options = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
units = ["inches", "yards", "miles", "millimeters", "cm", "m", "km"]
print("Choose a conversion:")
for i in range(7):
    print(f"{i+1}. {units[i]}")
choice = int(input("Enter choice (1-7): "))
print(f"Converted length: {length * options[choice - 1]} {units[choice - 1]}")

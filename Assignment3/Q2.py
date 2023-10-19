humanAge = int(input("Enter your human age: "))
dogYears = 21 if humanAge >= 2 else humanAge * 10.5
if humanAge > 2:
    dogYears += (humanAge-2)*4
print("Dog years: ", dogYears)


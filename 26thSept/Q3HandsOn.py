rows = int(input("Enter the number of rows: "))
rows = rows+1
b = rows - 1
for row in range(0, rows):
    for blankspaces in range(0,b):
        print(" ", end = "")
    for stars in range(0,row):
        print("* ", end = "")
    b = b-1
    print("")

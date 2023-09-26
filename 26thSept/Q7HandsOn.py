ruler1 = "1"
rows = 5
for row in range(1, rows):
    finalString = "1 "
    for inc in range(2,row):
        finalString = finalString + str(inc)+ " " + ruler1 +" "
    for dec in range(row, 0, -1):
        finalString = finalString + str(dec)+ " " + ruler1 +" "
    print(finalString[:-4])

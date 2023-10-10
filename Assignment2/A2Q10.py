def SOED():
    sum = 0
    num = input("Enter num: ")
    d1 = int(num[0])
    d2 = int(num[1])
    d3 = int(num[2])
    d4 = int(num[3])
    if d1 % 2 == 0:
        sum = sum + d1
    if d2 % 2 == 0:
        sum = sum + d2
    if d3 % 2 == 0:
        sum = sum + d3
    if d4 % 2 == 0:
        sum = sum + d4
    print("Sum of even digits: ", sum)
SOED()

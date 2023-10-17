num = int(input("Enter a number: "))
def perfect(num):
    sum = 0
    for x in range(1,num):
        if num%x == 0:
            sum = sum + x 
    if sum == num:
        print("Perfect")
    else: print("Not perfect")

perfect(num)

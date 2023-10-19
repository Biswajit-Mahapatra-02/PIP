def cube_of_digits(number):
    return sum(int(digit)**3 for digit in str(number))
num = input()
if num == (str)(cube_of_digits(num)):
    print("Armstrong")
else: print("No")
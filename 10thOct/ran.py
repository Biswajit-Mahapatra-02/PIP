import random
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
a = random.randint(num1, num2)
print(f'A random number between {num1} and {num2} is {a}')
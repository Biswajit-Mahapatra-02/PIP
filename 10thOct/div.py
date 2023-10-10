import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
if(num1 % num2 == 0):
	print("The two numbers divide evenly")
else:
	print("The two numbers do not divide evenly")
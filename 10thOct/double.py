import sys
d1 = float(sys.argv[1])
d2 = float(sys.argv[2])
d3 = float(sys.argv[3])
if d1>d2>d3 or d1<d2<d3:
	print(True)
else:
	print(False)
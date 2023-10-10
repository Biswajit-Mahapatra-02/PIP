import sys
m = int(sys.argv[1])
d = int(sys.argv[2])

if (m==3 and d>=20) or (3<m<6) or (m==6 and d<=20):
	print(True)
else: print(False)
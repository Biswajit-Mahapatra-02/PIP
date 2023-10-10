def collinear(x1,y1,x2,y2,x3,y3):
    slope_12 = (y2-y1)/(x2 - x1) if(x2 - x1)!=0 else float('inf')
    slope_13 = (y3-y1)/(x3 - x1) if(x2 - x1)!=0 else float('inf')
    return slope_12 == slope_13
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))
print(collinear(x1,y1,x2,y2,x3,y3))

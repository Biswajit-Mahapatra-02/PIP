a = int(input())
b = int(input())
c = int(input())
def max2(a,b):
    if a > b:
        return a
    else: return b
def max3(a,b,c):
    m = max2(a,b)
    om = max2(m, c)
    print(om)
max3(a,b,c)

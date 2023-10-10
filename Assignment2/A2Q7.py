import math
def areaTriangle(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def main():
    side1 = int(input('Side1: '))
    side2 = int(input('Side2: '))
    side3 = int(input('Side3: '))
    assert side1 + side2 > side3
    assert side1 + side3 > side2
    assert side2 + side3 > side1
    print(f"The area of the triangle with sides {side1}, {side2} and {side3} is: {areaTriangle(side1, side2, side3)}")
    
main()

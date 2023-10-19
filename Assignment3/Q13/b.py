import math

def series_b(x, n):
    result = 0
    for i in range(n+1):
        term = (x**i) / math.factorial(i)
        result += term
    return result
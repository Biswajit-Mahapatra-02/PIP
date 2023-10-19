import math

def series_a(x, n):
    result = 0
    for i in range(n+1):
        term = ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
        result += term
    return result
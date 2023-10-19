def are_coprimes(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    return gcd(a, b) == 1
if are_coprimes(int(input()), int(input())):
    print("Co prime")
else: print("no")
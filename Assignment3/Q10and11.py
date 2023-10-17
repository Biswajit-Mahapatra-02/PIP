def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

def lcm(a,b):
    return (a*B)//gcd(a,b)

a = int(input('Enter a num: '))
b = int(input('Enter a num: '))
print(f'The lcm is: {lcm(a,b)}')
print(f'The gcd is: {gcd(a,b)}')

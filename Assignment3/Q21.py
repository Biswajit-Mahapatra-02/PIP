def get_prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def main():
    n = int(input("Enter an integer (2 or greater): "))

    if n < 2:
        print("Error: Value must be 2 or greater.")
    else:
        prime_factors = get_prime_factors(n)

        print(f"The prime factors of {n} are:")
        for factor in prime_factors:
            print(factor)

main()
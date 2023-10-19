def print_pattern(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * (2 * i - 1))

print_pattern(4)
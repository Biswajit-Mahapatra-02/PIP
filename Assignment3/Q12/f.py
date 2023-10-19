def print_pattern(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("*", " "*(2*n-5), "*")

print_pattern(6)
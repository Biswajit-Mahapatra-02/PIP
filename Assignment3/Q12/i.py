def odd(n):
    return 2*n - 1
def print_pattern(num):
    n = odd(num)  # Number of rows
    spaces = 0
    midspace = n
    for i in range(num, 0, -1):
        if i == num:
            print("* " * n)
            spaces += 2
            continue;
        print(" "*spaces, end = "")
        spaces += 2
        if i != 1 and i != n:
            print("*", end = "")
            print(" "*midspace, end="")
            print("*", end = "")
            midspace -= 4
        elif i == 1:
            print("*")
        print()

print_pattern(4)
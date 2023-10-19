def print_pattern(n):
    for i in range(1, n+1):
        print("  "*(n-i) + " ".join(str(j) for j in range(i, 0, -1)) + " " + " ".join(str(j) for j in range(2, i+1)))

print_pattern(4)

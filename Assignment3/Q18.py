def multiply_by_repeated_addition(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result
multiply_by_repeated_addition(int(input()))
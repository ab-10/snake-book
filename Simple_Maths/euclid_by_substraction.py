def greatest_common_divisor(a, b):
    # When a = b, we have reached the GCD
    if a == b:
        return a
    # At every recursive step, 
    # b = min(a, b) and a = max - min
    elif a > b:
        return greatest_common_divisor(a - b, b)
    elif a < b:
        return greatest_common_divisor(b - a, a)

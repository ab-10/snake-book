def greatest_common_divisor(a, b):
    # If b is 0, we reached the GCD
    if b == 0:
        return a
    else:
        # At every recursive step
        # a = b and b = a % b
        return greatest_common_divisor(b, a % b)

def logarithmic_exponentiation(base, power):
    # If power == 1, then we only need to return the base
    if power == 1:
        return base

    result = 1
    while power != 1:
        # While power is even, we divide it by 2 and we
        # multiply result by  the base squared
        while power % 2 == 0:
            result *= base * base
            power = power / 2
        # When we get here, power is an odd number
        # so we only multiply by base (as long as power is not 1)
        if power > 1:
            result *= base
            power = power - 1

    return result


print("1 ^ 90 is %d" % logarithmic_exponentiation(1, 90))
print("2 ^ 5 is %d" % logarithmic_exponentiation(2, 5))
print("100 ^ 1 is %d" % logarithmic_exponentiation(100, 1))
print("5 ^ 20 is %d" % logarithmic_exponentiation(5, 20))

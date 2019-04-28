def logarithmic_exponentiation(base, power):
    result = 1
    while power > 0:
        # While power is even, we divide it by 2 and we
        # multiply result by  the base squared
        while power % 2 == 0:
            power = power / 2
            base = base * base
        # When we get here, power is an odd number
        # so we only multiply by base
        result *= base
        power = power - 1

    return result


print("1 ^ 90 is %d" % logarithmic_exponentiation(1, 90))
print("2 ^ 5 is %d" % logarithmic_exponentiation(2, 5))
print("100 ^ 1 is %d" % logarithmic_exponentiation(100, 1))
print("5 ^ 20 is %d" % logarithmic_exponentiation(5, 20))

# Find the primes until limit
def sieve_of_erathostenes(limit):
    # We need a list with 'limit' elements.
    # We will mark 1 to mean 'prime' and 0 to mean 'not prime'
    # (or vice versa, it's arbitrary)
    primes = []
    for index in xrange(limit):
        # In the beginning, we initialise the list with 1s
        # except for:
        # - even numbers (greater than 2)
        # - one (it's not prime by convention)
        if (index % 2 == 0 and index != 2) or index == 1:
            primes.append(0)
        else:
            primes.append(1)

    # Now, for numbers greater than 2 (multiples of 2
    # are already marked as composite) that are marked
    # as prime (primes[number] == 1) we mark all their
    # multiples as non-prime

    # We only need to go until limit / 2 since after
    # that the multiples would go over the limit
    for number in xrange(limit/2):
        # If the number is prime
        if primes[number] == 1:
            # Start from 3 since all even numbers have already
            # been sieved
            multiplication_factor = 3
            while number * multiplication_factor < limit:
                primes[number * multiplication_factor] = 0
                # We only need to look the odd multiplication factors
                multiplication_factor += 2

    # Thus, the remaining numbers marked by 1 are all prime
    return primes


def is_it_prime(number, primes):
    if primes[number] == 1:
        print("%d is prime." % number)
    else:
        print("%d is not prime." % number)


primes = sieve_of_erathostenes(100000)
is_it_prime(1, primes)
is_it_prime(5, primes)
is_it_prime(9, primes)
is_it_prime(113, primes)
is_it_prime(300, primes)
is_it_prime(4367, primes)

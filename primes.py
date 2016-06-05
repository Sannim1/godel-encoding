import math

def generate_primes(required_number_of_primes = 20):
    i = 0
    primes = []
    prime_count = 0
    while prime_count < required_number_of_primes:
        i += 1;
        if is_prime(i):
            primes.append(i)
            prime_count += 1

    return primes

def is_prime(number):
    if number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in xrange(2, int(math.ceil(math.sqrt(number))) + 1):
        if number % i == 0:
            return False

    return True

generate_primes()
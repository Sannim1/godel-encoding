import primes
import utils

def decode(encoded_sentence):
    plaintext = []
    godel_codes = encoded_sentence.split("|")

    for godel_code in godel_codes:
        plaintext.append(make_word_from_godel_code(godel_code))

    return " ".join(plaintext)

def make_word_from_godel_code(godel_code):
    word = ""
    factor_count = factorize(to_int(godel_code))

    factors = factor_count.keys()
    factors.sort()

    for factor in factors:
        word += get_char_from_alphabet(factor_count[factor])

    return word

def get_char_from_alphabet(char_index):
    alphabet = utils.make_alphabet()

    return alphabet[char_index - 1]


def factorize(number):
    factor_counter = {}
    factor = 2
    while factor <= number:
        if (not primes.is_prime(factor)):
            factor += 1

        if (number % factor == 0):
            # we are dealing with a prime factor
            if (not factor_counter.has_key(factor)):
                factor_counter[factor] = 0

            factor_counter[factor] = factor_counter[factor] + 1

            number = number / factor

            if (number % factor != 0):
                factor += 1

    return factor_counter

def to_int(number):
    try:
        return int(number)
    except ValueError:
        # for hexadecimal numbers
        return int(number, 16)

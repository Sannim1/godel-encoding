import primes
import utils

def encode(sentence):
    sentence = " ".join(sentence.splitlines())
    words = sentence.split(" ")
    longest_word_length = 0

    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)

    required_primes = primes.generate_primes(longest_word_length)

    godel_words = []
    for word in words:
        godel_word = make_godel_word(word, required_primes)
        godel_words.append(str(godel_word))

    return "|".join(godel_words)

def make_godel_word(word, required_primes):
    godel_number = 1
    for index in range(len(word)):
        char = word[index]
        alphabet_index = get_alphabet_index(char)
        godel_number = godel_number * (required_primes[index] ** alphabet_index)

    return godel_number

def get_alphabet_index(char):
    alphabet = utils.make_alphabet()

    return alphabet.index(char) + 1

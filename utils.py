def make_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # add special characters
    for i in xrange(33, 48):
        alphabet += chr(i)

    for i in xrange(58, 65):
        alphabet += chr(i)

    for i in xrange(91, 97):
        alphabet += chr(i)

    for i in xrange(123, 127):
        alphabet += chr(i)

    return alphabet
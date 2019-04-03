#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)

    # CHEAT
    #     result = int(digits, base)

    # if base == 2:
    #
    #     result = 0
    #     power = 0
    #
    #     for char in reversed(digits):
    #
    #         if char == '0':
    #             power += 1
    #             print("CURRENT POWER => {}".format(power))
    #         else:
    #             result += pow(base, power)
    #             power += 1
    #             print("RESULT => {}".format(result))
    #
    #     return result


    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...
    digits = digits.lower()
    max_digits = string.digits + string.ascii_lowercase
    base_digits = max_digits[:base]

    result_arr = []
    power = 0

    for char in reversed(digits):
        number = base_digits.index(char) * (base ** power)
        result_arr.append(number)
        power += 1

    result = sum(result_arr)
    print("RESULT => {}".format(result))
    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
    max_digits = string.digits + string.ascii_lowercase
    base_digits = max_digits[:base]
    result = ""

    if number == base:
        result = '10'
        return result

    if number < base:   
        remainder = number % base
        result = base_digits[int(remainder)] + result
        return result

    while number > base:
        remainder = number % base
        result = base_digits[int(remainder)] + result
        number = number / base

    if number == base:
        result = '10' + result
        return result

    remainder = number % base
    result = base_digits[int(remainder)] + result


    print("RESULT => {}".format(result))
    return result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # decode(digits, base1)
    encode(16, 16)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

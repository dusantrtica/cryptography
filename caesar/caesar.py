ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3


def char_to_number(c):
    return ALPHABET.index(c)


def number_to_char(num):
    return ALPHABET[num]


def translate_for_key(index_of_char):
    return (index_of_char + KEY) % 26


def caesar_encrypt(plain_text):
    char_indeces = map(char_to_number, plain_text)
    translated_keys = map(translate_for_key, char_indeces)
    new_chars = map(number_to_char, translated_keys)

    return "".join(new_chars)


def caesar_decrypt(cipher):
    pass


import unittest


class TestCaesar(unittest.TestCase):
    def test_caesar_encrypt(self):
        self.assertEqual("KHOOR", caesar_encrypt("HELLO"))


if __name__ == "__main__":

    unittest.main()

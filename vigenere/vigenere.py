ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def char_to_number(c):
    return ALPHABET.find(c)


def number_to_char(num):
    if num == -1:
        return ' '
    return ALPHABET[num]


def translate_char_with(index_of_char, key):    
    if index_of_char != -1:
        return (index_of_char + key) % 26
    return -1

def vigenere_encrypt(plain_text, key):
    char_indices = map(char_to_number, plain_text)
    key_len = len(key)
    translated_keys = map(lambda enum : translate_char_with(enum[1], char_to_number(key[enum[0] % key_len])), enumerate(char_indices))
    new_chars = map(number_to_char, translated_keys)

    return "".join(new_chars)

def vigenere_decrypt(cipher, key): 
    char_indices = map(char_to_number, cipher)
    key_len = len(key)
    translated_keys = map(lambda enum : translate_char_with(enum[1], -char_to_number(key[enum[0] % key_len])), enumerate(char_indices))
    new_chars = map(number_to_char, translated_keys)

    return "".join(new_chars)

import unittest

class TestVigenere(unittest.TestCase):
    def test_vigenere_encrypt(self):
        self.assertEqual("LLKJ BK C QXKWCXI", vigenere_encrypt('THIS IS A MESSAGE', 'SECRET'))
    
    def test_vigenere_decrypt(self):
        self.assertEqual("THIS IS A MESSAGE", vigenere_decrypt('LLKJ BK C QXKWCXI', 'SECRET'))

if __name__ == '__main__':
    unittest.main()
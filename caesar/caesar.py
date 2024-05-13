ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3


def char_to_number(c):
    return ALPHABET.index(c)


def number_to_char(num):
    return ALPHABET[num]


def translate_char_with(key): 
    def translate(index_of_char):
        return (index_of_char + key) % 26

    return translate


def caesar_encrypt(plain_text):
    char_indices = map(char_to_number, plain_text)
    translated_keys = map(translate_char_with(KEY), char_indices)
    new_chars = map(number_to_char, translated_keys)

    return "".join(new_chars)


def caesar_decrypt(cipher):
    char_indices = map(char_to_number, cipher)
    translated_keys = map(translate_char_with(-KEY), char_indices)
    new_chars = map(number_to_char, translated_keys)

    return "".join(new_chars)
    
def crack_caesar(cipher):
    # Crack the cipher based on frequency analisys
    frequencies = [0 for _ in range(len(ALPHABET))]
    for c in cipher:
        if c != ' ':
            frequencies[ALPHABET.index(c)] += 1
    max_cnt = max(frequencies)
    max_cnt_index = 0
    for index, elem in enumerate(frequencies):
        if elem == max_cnt:
            max_cnt_index = index
            break

    key = max_cnt_index - ALPHABET.index('E')

    return key



import unittest


class TestCaesar(unittest.TestCase):
    def test_caesar_encrypt(self):
        self.assertEqual("KHOOR", caesar_encrypt("HELLO"))

    def test_caesar_decrypt(self):
        self.assertEqual('HELLO', caesar_decrypt('KHOOR'))

    def test_crack_caesar(self):
        key = crack_caesar('Pm ol ohk  hufaopun jvumpkluaphs av zhf ol dyval pa pu jpwoly aoha pz if zv johunpun aol vykly vm aol slaalyz vm aol hswohila aoha uva h dvyk jvbsk il thkl vba'.upper())

        key = crack_caesar('If he had anything confidential to say he wrote it in cipher that is by so changing the order of the letters of the alphabet that not a word could be made out'.upper())
        


if __name__ == "__main__":

    unittest.main()

import pytest
from encryption import letter_shift, word_encrypt, sentence_encrypt, file_encrypt
import os


def test_letter_shift():
    assert letter_shift('a', 2) == 'c'
    assert letter_shift('z', -2) == 'x'
    assert letter_shift('a', -1) == 'z'
    assert letter_shift('a', 28) == 'c'
    assert letter_shift('A', 2) == 'C'
    assert letter_shift(1, 1) == 1

def test_word_encrypt():
    assert word_encrypt('abc', 2) == 'cde'
    assert word_encrypt('text', 7) == 'alea'
    assert word_encrypt('maintenance', 27) == 'nbjoufobodf'
    assert word_encrypt('MainTenancE', 27) == 'NbjoUfobodF'
    assert word_encrypt('aB3', 2) == 'cD3'

def test_sentence_encrypt():
    assert sentence_encrypt('abc def ghi', 2) == 'cde fgh ijk'

def test_file_encrypt():
    file_encrypt('test.txt',3)
    new_file = 'encrypted_test.txt'
    assert new_file in os.listdir()

    with open(new_file, 'r') as f:
        info = f.readlines()
    assert info[0] == "Wklv lv d vhqwhqfh\n"
    os.remove(new_file)
import pytest
from encryption import letter_shift, word_encrypt, sentence_encrypt, file_encrypt
import os


@pytest.mark.parametrize('letter, shift, output',[('a', 2, 'c'),('z', -2, 'x'), ('a', -1, 'z'), ('a', 28, 'c'), ('A', 2, 'C'),(1,1,1)])
def test_letter_shift(letter, shift, output):
    assert letter_shift(letter, shift) == output

@pytest.mark.parametrize('string, shift, output', [('abc', 2, 'cde'),('text', 7, 'alea'), ('maintenance', 27, 'nbjoufobodf'),
('MainTenancE', 1, 'NbjoUfobodF'), ('aB3', 2, 'cD3')])
def test_word_encrypt(string, shift, output):
    assert word_encrypt(string, shift) == output

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
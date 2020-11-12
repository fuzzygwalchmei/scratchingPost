import pytest
from decryption import word_decrypt, sentence_decrypt, file_decrypt
from encryption import file_encrypt
import os



def test_word_encrypt():
    assert word_decrypt('cde', 2) == 'abc'
    assert word_decrypt('alea', 7) == 'text'
    assert word_decrypt('nbjoufobodf', 27) == 'maintenance'
    assert word_decrypt('NbjoUfobodF', 27) == 'MainTenancE'
    assert word_decrypt('cD3', 2) == 'aB3'

def test_sentence_encrypt():
    assert sentence_decrypt('cde fgh ijk', 2) == 'abc def ghi'

def test_file_encrypt():
    file_encrypt('test.txt',3)
    file_decrypt('encrypted_test.txt',3)
    new_file = 'decrypted_test.txt'
    assert new_file in os.listdir()

    with open(new_file, 'r') as f:
        info = f.readlines()
    assert info[0] == "This is a sentence\n"
    os.remove(new_file)
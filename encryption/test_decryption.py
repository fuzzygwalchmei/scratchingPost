import pytest
from decryption import word_decrypt, sentence_decrypt, file_decrypt
from encryption import file_encrypt
import os


@pytest.mark.parametrize('string, shift, output',[('cde', 2,'abc'), ('alea', 7,'text'),('nbjoufobodf', 27, 'maintenance'), 
('NbjoUfobodF', 27, 'MainTenancE'), ('cD3', 2, 'aB3')])
def test_word_decrypt(string, shift, output):
    assert word_decrypt(string, shift) == output

def test_sentence_decrypt():
    assert sentence_decrypt('cde fgh ijk', 2) == 'abc def ghi'

def test_file_decrypt():
    file_encrypt('test.txt',3)
    file_decrypt('encrypted_test.txt',3)
    new_file = 'decrypted_test.txt'
    assert new_file in os.listdir()

    with open(new_file, 'r') as f:
        info = f.readlines()
    assert info[0] == "This is a sentence\n"
    os.remove(new_file)
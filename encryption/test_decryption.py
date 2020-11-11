import pytest
from decryption import word_decrypt, sentence_decrypt


def test_word_encrypt():
    assert word_decrypt('cde', 2) == 'abc'
    assert word_decrypt('alea', 7) == 'text'
    assert word_decrypt('nbjoufobodf', 27) == 'maintenance'
    assert word_decrypt('NbjoUfobodF', 27) == 'MainTenancE'
    assert word_decrypt('cD3', 2) == 'aB3'

def test_sentence_encrypt():
    assert sentence_decrypt('cde fgh ijk', 2) == 'abc def ghi'
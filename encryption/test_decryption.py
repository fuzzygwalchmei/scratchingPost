import pytest
from decryption import word_decrypt


def test_word_encrypt():
    assert word_decrypt('cde', 2) == 'abc'
    assert word_decrypt('alea', 7) == 'text'
    assert word_decrypt('nbjoufobodf', 27) == 'maintenance'
    assert word_decrypt('NbjoUfobodF', 27) == 'MainTenancE'
    assert word_decrypt('cD3', 2) == 'aB3'
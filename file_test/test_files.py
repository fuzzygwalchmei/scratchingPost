import pytest
import os
import files



def test_file_create():
    files.create_file('test1.txt')
    assert 'test_file.txt' in os.listdir()



def test_file_open():
    pass



def test_file_read():
    info = files.read_file("test_file.txt")
    assert info[0] == "Line 1"



def test_file_write():
    files.write_file("test_file.txt", "\nnew line")
    info = files.read_file("test_file.txt")
    assert info[-1] == "new line"




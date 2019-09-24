import math_func

def test_add():
    assert math_func.add(2,3) == 5

def test_add2():
    assert math_func.add("test","func") == "testfunc"
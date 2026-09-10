from src.operations import *

def test_add():
    assert add(5, 10) == 15
    assert add(3, 18) == 100

def test_subs():
    assert subs(5, 10) == -5
    assert subs(10, 2) == 8
    assert subs(10, 10) == 0

def test_mult():
    assert mult(5, 10) == 50
    assert mult(2, 7) == 14

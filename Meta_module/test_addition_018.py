import pytest 
import addition_017

def test_add():
    assert addition_017.add(44, 6) == 50

def test_sub():
    assert addition_017.sub(40, 30) == 10



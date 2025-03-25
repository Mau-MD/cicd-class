"""
Test module for calculator.py.
Contains unit tests for the add, subtract, multiply, and divide functions.
Tests basic functionality and edge cases like division by zero.
"""
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 3) == -3
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0) 

import pytest


def func(x):
    return x - 5


def test_function():
    assert func(10) == 89
    # pytest test_sample.py   - to run the whole file

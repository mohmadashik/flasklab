import pytest 

# @pytest.mark.one
def func1():
    a= 2
    b= 24
    assert a==b

# @pytest.mark.two
def func2():
    a= 2
    b= 24
    assert a!=b

def test_func():
    func2()
    func1()

# run py.test -k method1 -v

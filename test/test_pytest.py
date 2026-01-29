import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98

def test_fun5():
    assert calculator.fun5(10, 2) == 5.0
    assert calculator.fun5(9, 3) == 3.0
    assert calculator.fun5(-10, 2) == -5.0
    assert calculator.fun5(7, 2) == 3.5
    
    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.fun5(5, 0)

def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 2) == 25
    assert calculator.fun6(10, 0) == 1
    assert calculator.fun6(2, -1) == 0.5

def test_fun7():
    assert calculator.fun7(10, 3) == 1
    assert calculator.fun7(15, 4) == 3
    assert calculator.fun7(20, 6) == 2
    
    # Test modulo by zero
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        calculator.fun7(5, 0)

def test_fun8():
    assert calculator.fun8(0) == 1
    assert calculator.fun8(1) == 1
    assert calculator.fun8(5) == 120
    assert calculator.fun8(4) == 24
    assert calculator.fun8(3) == 6
    
    # Test negative factorial
    with pytest.raises(ValueError, match="Factorial not defined for negative"):
        calculator.fun8(-5)
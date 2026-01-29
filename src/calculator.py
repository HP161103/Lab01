def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """ 
    total_sum = x + y + z
    return total_sum


# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)


def fun5(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: Result of x divided by y.
    Raises:
        ValueError: If y is zero or if inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def fun6(x, y):
    """
    Calculates x to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        int/float: Result of x raised to power y.
    Raises:
        ValueError: If inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y

def fun7(x, y):
    """
    Calculates modulo (remainder of x divided by y).
    Args:
        x (int/float): Dividend.
        y (int/float): Divisor.
    Returns:
        int/float: Remainder of x divided by y.
    Raises:
        ValueError: If y is zero or if inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Cannot modulo by zero.")
    return x % y

def fun8(x):
    """
    Calculates factorial of x.
    Args:
        x (int): Non-negative integer.
    Returns:
        int: Factorial of x.
    Raises:
        ValueError: If x is negative or not an integer.
    """
    if not isinstance(x, int):
        raise ValueError("Input must be an integer.")
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
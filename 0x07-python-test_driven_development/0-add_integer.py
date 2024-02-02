#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """Cast the data type of num parameter

    Args:
        num (:obj:`int, float`): The number to cast.

    Returns:
        int: The number casted to integer.
    """
    if type(num) is float:
        num = int(num)
        return num

    return num

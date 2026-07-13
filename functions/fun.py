def squared(x: int):
    """
    Returns the square of a given integer.

    Parameters:
    x (int): The integer to be squared.

    Returns:
    int: The square of the input integer.
    """
    return x * x

print(squared(5))  # Example usage of the squared function

def add_numbers(a: int, b: int):
    """
    Returns the sum of two given integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of the two input integers.
    """
    return a + b

print(add_numbers(3, 4))  # Example usage of the add_numbers function

def even_odd(num: int):
    """
    Determines whether a given integer is even or odd.

    Parameters:
    num (int): The integer to be checked.

    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(5))  # Example usage of the even_odd function
print(even_odd(6))  # Example usage of the even_odd function
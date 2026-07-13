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


# find max
def find_max(lst: list):
    """
    Returns the maximum value from a given list of integers.

    Parameters:
    lst (list): The list of integers.

    Returns:
    int: The maximum value in the list.
    """
    if not lst:
        return None  # Return None if the list is empty
    return max(lst)

print(find_max([1, 5, 3, 9, 2]))  # Example usage of the find_max function


#  max of 3 numbers

def max_of_three(a: int, b: int, c: int):
    """
    Returns the maximum value among three given integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.

    Returns:
    int: The maximum value among the three integers.
    """
    return max(a, b, c)

print(max_of_three(1, 5, 3))  # Example usage of the max_of_three function

def greet(name: str, age: int) -> str:
    print(f"Hello, {name}! You are {age} years old.")

greet("Bob", 12)

# factorial of a number
def factorial(n: int) -> int:
    """
    Returns the factorial of a given non-negative integer.

    Parameters:
    n (int): The non-negative integer to calculate the factorial of.

    Returns:
    int: The factorial of the input integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
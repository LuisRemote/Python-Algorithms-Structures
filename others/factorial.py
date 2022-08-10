# Recursion in Python: Defining a Recursive Function

"""
n! = n * (n - 1) * (n -2) * (n - 3) * ... * 1
n! = n * (n - 1)!
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!
0! = 1
"""

def factorial_recursive(n: int) -> int:
    """Docstring"""

    # Base case
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)



print(factorial_recursive(5))


def fibonacci(n):
    """Return the Fibonacci number for num
    >>> fibonacci(1)
    1
    >>> fibonacci(12)
    144
    """
    from math import sqrt
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
import math


def calculate_cuadratic_roots(a, b, c):
    if type(a) is not float and type(a) is not int:
        raise TypeError("Coefficient 'a' must be a number")

    if type(b) is not float and type(b) is not int:
        raise TypeError("Coefficient 'b' must be a number")

    if type(c) is not float and type(c) is not int:
        raise TypeError("Coefficient 'c' must be a number")

    if a == 0:
        raise ValueError("Coefficient 'a' can not be equal to zero")

    discr = b ** 2 - 4 * a * c
    if (discr < 0):
        return None

    root1 = (-b + math.sqrt(discr)) / (2 * a)
    root2 = (-b - math.sqrt(discr)) / (2 * a)

    return (root1, root2)

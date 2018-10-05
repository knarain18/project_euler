"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 325 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_differences(n):
    """
    >>> sum_square_differences(10)
    2640
    """
    ind_square_sum = []
    for num in range(n+1):
        num = num**2
        ind_square_sum.append(num)

    squares = sum(ind_square_sum)
    square_sum = ((n*(n+1))//2)**2
    return square_sum - squares

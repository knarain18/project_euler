def largest_prime_factor(n):
    """
    >>> largest_prime_factor(5679)
    631
    >>> largest_prime_factor(4568)
    571
    """
    basic_primes = [2,3,5,7]
    if n % 2 == 0:
        i = n//2
        for p in basic_primes:
            while i % p == 0:
                i = i//p
    if n % 3 == 0:
        i = n//3
        for p in basic_primes:
            while i % p == 0:
                i = i//p
    if n % 5 == 0:
        i = n//5
        for p in basic_primes:
            while i % p == 0:
                i = i//p
    if n % 7 == 0:
        i = n//7
        for p in basic_primes:
            while i % p == 0:
                i = i//p
    return i


def is_prime(n):
    """
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    """
    h = 2
    while n % h != 0 and h <= n:
        h += 1
        if h == n:
            return True
    return False


def max_prime_factor(n):
    """
    >>> max_prime_factor(5679)
    631
    >>> max_prime_factor(4568)
    571
    """
    max = None
    for i in range(2,n+1):
        if is_prime(i) == True:
            if n % i == 0:
                max = i
    return max

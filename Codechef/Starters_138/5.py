from itertools import combinations
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_sum_of_squares(n):
    primes = [p for p in range(2, int(sqrt(n)) + 1) if is_prime(p)]
    prime_combinations = combinations(primes, 3)

    for a, b, c in prime_combinations:
        if a**2 + b**2 + c**2 == n:
            return a, b, c

    return None

# Test the function
for _ in range(int(input())):
    n = int(input())
    result = find_prime_sum_of_squares(n)
    if result:
        print("yes")
    else:
        print("no")
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_pair(A, N):
    even = -1
    odd = -1
    
    for i in range(N):
        if A[i] % 2 == 0:
            if even == -1:
                even = i
            else:
                return even + 1, i + 1
        else:
            if odd == -1:
                odd = i
            else:
                if not isPrime(A[odd] + A[i]):
                    return odd + 1, i + 1
    
    if even != -1 and odd != -1:
        if not isPrime(A[even] + A[odd]):
            return even + 1, odd + 1
    
    return -1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        result = find_pair(A, N)
        if result == -1:
            print(-1)
        else:
            print(result[0], result[1])

if __name__ == "__main__":
    main()

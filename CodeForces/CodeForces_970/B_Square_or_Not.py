import math

import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def is_perfect_square(x):
    root = int(math.sqrt(x))
    return root * root == x

def can_be_squared(s, n):
    r = int(math.sqrt(n))
    
    if s[0:r] != '1' * r or s[-r:] != '1' * r:
        return "No"
    
    for i in range(1, r-1):
        if s[i*r] != '1' or s[(i+1)*r - 1] != '1':
            return "No"
    
    for i in range(1, r-1):
        if s[i*r+1:(i+1)*r-1] != '0' * (r-2):
            return "No"
    
    return "Yes"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        if not is_perfect_square(n):
            print("No")
        else:
            print(can_be_squared(s, n))

if __name__ == "__main__":
    main()





import sys
from collections import defaultdict, deque,Counter
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        if n % 2 == 0:
            even_count = Counter(s[::2])
            odd_count = Counter(s[1::2])
            max_even = max(even_count.values(), default=0)
            max_odd = max(odd_count.values(), default=0)
            print((n // 2 - max_even) + (n // 2 - max_odd))
        else:
            even_count = Counter(s[::2])
            odd_count = Counter(s[1::2])
            mini = float('inf')
            
            for i in range(n):
                if i % 2 == 0:
                    even_count[s[i]] -= 1
                    if even_count[s[i]] == 0:
                        del even_count[s[i]]
                else:
                    odd_count[s[i]] -= 1
                    if odd_count[s[i]] == 0:
                        del odd_count[s[i]]
                
                new_n = n - 1
                max_even = max(even_count.values(), default=0)
                max_odd = max(odd_count.values(), default=0)
                operations = (new_n // 2 - max_even) + (new_n // 2 - max_odd) + 1
                mini = min(mini, operations)
                
                if i % 2 == 0:
                    odd_count[s[i]] += 1
                else:
                    even_count[s[i]] += 1
            
            print(mini)

if __name__ == "__main__":
    main()
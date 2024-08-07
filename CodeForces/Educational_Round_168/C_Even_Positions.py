import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    test_cases = int(input())
    
    results = []

    for _ in range(test_cases):
        length = int(input())
        s = input().strip()

        stack = []
        stack.append(0)
        result = 0

        for i in range(1, length):
            if s[i] == '_':
                if stack:
                    result += i - stack.pop()
                else:
                    stack.append(i)
            elif s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    result += i - stack.pop()

        results.append(result)

    for res in results:
        print(res)       
        

if __name__ == "__main__":
    main()
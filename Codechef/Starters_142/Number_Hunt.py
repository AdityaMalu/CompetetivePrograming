#If input array is sorted then
#- Binary search
#- Two pointers

#If asked for all permutations/subsets then
#- Backtracking

#If given a tree then
#- DFS
#- BFS

#If given a graph then
#- DFS
#- BFS

#If given a linked list then
#- Two pointers

#If recursion is banned then
#- Stack

#If must solve in-place then
#- Swap corresponding values
#- Store one or more different values in the same pointer

#If asked for maximum/minimum subarray/subset/options then
#Dynamic programming

#If asked for top/least K items then
#- Heap
#- QuickSelect

#If asked for common strings then
#- Map

#Else
#- Map/Set for O(1) time & O(n) space
#- Sort input for O(nlogn) time and O(1) space
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = n 
        while True:
            if is_prime(i):
                break
            i += 1
        j = i + 1
        while True:
            if is_prime(j):
                break
            j += 1
        print(i*j)
        

if __name__ == "__main__":
    main()
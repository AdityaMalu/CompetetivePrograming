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



def main():
    T = int(input())
    for _ in range(T):
        X, Y, Z, K = map(int, input().split())
        result = 0
        for x in range(1, X + 1):
            for y in range(1, Y + 1):
                z = x * y
                possible = K // z
                if K % z == 0:
                    if possible < Z + 1:
                        result = max(result, (X - x + 1) * (Y - y + 1) * (Z - possible + 1))
        print(result)

if __name__ == "__main__":
    main()
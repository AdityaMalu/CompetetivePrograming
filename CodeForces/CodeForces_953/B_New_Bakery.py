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
    t = int(input())
    for _ in range(t):
        n,a,b = map(int, input().split())
        k_optimal = b - a + 0.5
        k1 = max(0, min(int(k_optimal), min(n, b)))
        k2 = max(0, min(int(k_optimal) + 1, min(n, b)))
        
        def calculate_revenue(k):
            modified_price_sum = k * (2 * b - k + 1) // 2
            remaining_revenue = (n - k) * a
            return modified_price_sum + remaining_revenue
        revenue1 = calculate_revenue(k1)
        revenue2 = calculate_revenue(k2)
        
        print(max(revenue1, revenue2))

if __name__ == "__main__":
    main()
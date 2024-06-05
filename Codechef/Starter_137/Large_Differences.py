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

def sum_diff(A):
    return sum(abs(A[i] - A[i+1]) for i in range(len(A)-1))

def main():
    t = int(input())
    for _ in range(t):
        N,K = map(int,input().split())
        A = list(map(int,input().split()))
        B = A.copy()
        initial_sum = sum(abs(A[i] - A[i+1]) for i in range(N-1))
    
        max_sum = initial_sum
    
        for i in range(N):
            A[i] = 1
            max_sum = max(max_sum, sum_diff(A))
            A[i] = K
            max_sum = max(max_sum, sum_diff(A))
            A[i] = B[i]

        print(max_sum)


if __name__ == "__main__":
    main()
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
        x = int(input())
        v = [0] * 31
        for i in range(30):
            if (x >> i) & 1:
                v[i] = 1
            else:
                v[i] = 0
        
        for i in range(30):
            if v[i] == 1 and v[i + 1] == 1:
                pos = i
                flag = 1
            else:
                flag = 0
            
            if flag:
                j = i
                while v[j] == 1:
                    v[j] = 0
                    j += 1
                v[j] = 1
                v[pos] = -1
        print(31)
        print(*v)

if __name__ == "__main__":
    main()


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
        n =  int(input())
        arr = list(map(int, input().split()))
        even = 0
        odd = 0
        for i in arr:
            if i%2 == 0:
                even+=1
            else:
                odd+=1
        if even == 0 or odd == 0:
            a = set()
            for i in range(57):
                a = set()
                for j in range(n):
                    a.add(arr[j]%(2**i))
                    if len(a) == 2:
                        ans = 2**i
                        break
                if len(a) ==2:
                    print(ans)
                    break 
        else:
            print(2)

if __name__ == "__main__":
    main()
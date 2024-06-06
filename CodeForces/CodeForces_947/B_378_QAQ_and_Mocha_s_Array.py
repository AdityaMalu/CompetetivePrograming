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
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        cnt = a[0]
        ind = -1
        for i in range(1,n):
            cnt1 = a[i]%cnt
            if cnt1 != 0:
                cnt1 = a[i]
                ind = i
                break
        if ind == -1:
            print("YES")
            continue
        for i in range(n):
            if a[i]%cnt != 0 and a[i]%cnt1 != 0:
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    main()
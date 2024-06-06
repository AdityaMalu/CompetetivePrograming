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
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=list(map(int,input().split()))
        
        a=[(a[i],i)for i in range(n)]
        b=[(b[i],i)for i in range(n)]
        c=[(c[i],i)for i in range(n)]
        a.sort(reverse=True)
        b.sort(reverse=True)
        c.sort(reverse=True)
        res=0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if a[i][1]!=b[j][1] and a[i][1]!=c[k][1] and b[j][1]!=c[k][1]:
                        res=max(res,a[i][0]+b[j][0]+c[k][0])
        print(res)

if __name__ == "__main__":
    main()
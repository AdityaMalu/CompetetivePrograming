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
        n,k = map(int, input().split())
        if n%2 == 0:
            #sum of odd numbers till n:
            maxi = ((n//2)**2)*2
        else:
            #sum of even numbers till n:
            maxi = (n//2)*(n//2 + 1)*2
        if k %2 ==1 or k > maxi:
            print("NO")
        else:
            print("YES")
            arr = []
            for i in range(n):
                arr.append(i+1)
            k = k//2
            
        


if __name__ == "__main__":
    main()
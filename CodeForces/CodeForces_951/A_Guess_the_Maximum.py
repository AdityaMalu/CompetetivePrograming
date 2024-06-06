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
        arr = list(map(int, input().split()))
        start,end,maxi =0,0,max(arr)
        while(start<=maxi):
            mid = (start+maxi)//2
            flag = True
            for i in range(n-1):
                if max(arr[i],arr[i+1])<=mid:
                        flag = False
                        break
            if flag:
                end = mid
                start = mid+1
            else:
                maxi = mid-1
        print(end)


if __name__ == "__main__":
    main()
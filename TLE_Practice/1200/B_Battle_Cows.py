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
        n,c = map(int, input().split())
        arr = list(map(int, input().split()))
        our_cow = arr[c-1]
        ans = 0
        for i in range(c):
            if arr[i] > our_cow:
                arr[c-1], arr[i] = arr[i], arr[c-1]
                break
        
        curr = max(arr[0],arr[1])
        if max(arr) == our_cow:
            print(n-1)
        else:
            if curr == our_cow:
                ans = 1
            for i in range(2,n):
                # if i == c-1:
                #     continue
                if max(arr[i],curr) == our_cow:
                    ans+=1
                curr = max(curr,arr[i])
                            
            print(ans)
        


if __name__ == "__main__":
    main()
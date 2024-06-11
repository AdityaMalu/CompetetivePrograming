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

def readList():
  return list(map(int,input().split()))
 
def solve():
    n , m = readList()
    cards = defaultdict(list)
    for _ in range(n):
        cur = readList()
    
        for i in range(m):
            cards[i].append(cur[i])
    for i in cards:
        cards[i].sort()
        
    ans = 0
    for i in cards:
        pre_sum = cards[i][0]
        for j in range(1, n):
            ans += abs(cards[i][j] * j - pre_sum)
            pre_sum += cards[i][j]
        
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
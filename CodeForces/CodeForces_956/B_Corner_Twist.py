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
        n, m = map(int, input().strip().split())
        a = []
        for i in range(n):
            a.append(list(input()))      
        b = []
        for _ in range(n):
            b.append(list(input()))
        for i in range(n):
            for j in range(m):
                a[i][j] = int(a[i][j])
                b[i][j] = int(b[i][j])
        results = []
        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                if a[i][j] == b[i][j]:
                    continue
                else:
                    temp = (b[i][j] - a[i][j] + 3) % 3
                    temp2 = 2 * temp
                    a[i][j] = b[i][j]
                    a[i - 1][j - 1] = (a[i - 1][j - 1] + temp) % 3
                    a[i][j - 1] = (a[i][j - 1] + temp2) % 3
                    a[i - 1][j] = (a[i - 1][j] + temp2) % 3
        
        is_possible = True
        for i in range(n):
            if a[i][0] != b[i][0]:
                is_possible = False
                break
        
        for j in range(m):
            if a[0][j] != b[0][j]:
                is_possible = False
                break
        
        results.append("YES" if is_possible else "NO")
    
        print("\n".join(results))

if __name__ == "__main__":
    main()
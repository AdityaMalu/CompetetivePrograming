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
    for _ in range(int(input())):
        n, m = map(int, input().split())

        mat = [[int(x) for x in input().split()] for y in range(n)]

        for i in range(n):
            for j in range(m):

                mx = 0
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for nei in neighbors:
                    if (nei[0]<0 or nei[0] > n-1 or nei[1] < 0 or nei[1] > m-1):
                        continue
                    mx = max(mx, mat[nei[0]][nei[1]])
                if (mat[i][j] > mx):
                    mat[i][j] = mx

        for row in mat:
            print(*row)

if __name__ == "__main__":
    main()
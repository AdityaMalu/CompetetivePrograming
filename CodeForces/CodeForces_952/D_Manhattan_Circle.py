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
        n,m = map(int, input().split())
        matrix = []
        for i in range(n):
            matrix.append(input())
        hash_tags = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '#':
                    hash_tags.append((i,j))
        x,y = (hash_tags[0][0]+hash_tags[-1][0])//2+1, (hash_tags[0][1]+hash_tags[-1][1])//2+1
        print(x,y)

if __name__ == "__main__":
    main()
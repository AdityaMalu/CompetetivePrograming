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
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        s = list(data[index])
        index += 1
        a = list(map(int, data[index:index + m]))
        index += m
        c = list(data[index])
        index += 1
    
        a_sorted = sorted(set(a))
        c_sorted = sorted(c)
        
        for i in range(len(a_sorted)):
            s[a_sorted[i] - 1] = c_sorted[i]
        
        results.append("".join(s))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
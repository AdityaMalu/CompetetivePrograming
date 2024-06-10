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
        set1 = sorted(list(set((arr))))
        ans = []
        dict1 = defaultdict(int)
        for i in range(len(arr)):
            dict1[arr[i]]+=1
        dict1 = dict(sorted(dict1.items()))
        if n == 2:
            ans = [arr[0],arr[0]]
            pass
        else:
            j = 0
            for i in range(n-1,-1,-1):
                try: 
                    if dict1[set1[j]]>0:
                        ans.append(set1[j])
                        dict1[set1[j]]-=i
                    if dict1[set1[j]]==0:
                        j+=1
                except:
                    pass
            ans.append(max(arr))

        print(*ans)
            
        

if __name__ == "__main__":
    main()
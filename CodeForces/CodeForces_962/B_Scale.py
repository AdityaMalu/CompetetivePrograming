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
        matrix = []
        ans = []
        for i in range(n):
            matrix.append(list(input()))
            
        for i in range(0,n,k):
            temp = []
            for j in range(0,n,k):
                temp.append(matrix[i][j])
            ans.append(temp)
        
        for i in range(len(ans)):
            print("".join(ans[i]))
        

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def prefix_cnt_1(s):
    cnt = 0
    result = [0]*len(s)
    for i in range(len(s)):
        result[i] = cnt
        if s[i] == "1":
            cnt += 1
    return result

def inversions(s):
    pre = prefix_cnt_1(s)
    res = 0
    for i in range(len(s)):
        if s[i] == "0":
            res += pre[i]
    return res

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        s = list(input())
        result = float('inf')
        cnt = k
        one_ind = []
        for i in range(n):
            if cnt == 0:
                break
            if s[i] == "1":
                one_ind.append(i)
                s[i] = "0"
                cnt -= 1
                
        result = min(result,inversions(s))

        for i in range(n-1,-1,-1):
            if(len(one_ind) == 0):
                break
            if s[i] == "0":
                s[i] = "1"
                s[one_ind[-1]] = "1"
                one_ind.pop(-1)
                result = min(result,inversions(s))
        print(result)

        
                       
if __name__ == "__main__":
    main()
# Link : https://codeforces.com/contest/1955/problem/C

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
        arr = list(map(int, input().split()))
        pre = [arr[0]]
        suf = [arr[-1]]
        ans = 0
        for i in range(1,n):
            pre.append(pre[-1] + arr[i])
            suf.append(suf[-1] + arr[n-i-1])
        if k%2==0:
            k1 = k//2
            k2 = k//2
        else:
            k1 = k//2+1
            k2 = k//2 
        i = 0
        if(sum(arr)<=k):
            print(n)
            continue
        while(pre[i]<=k1):
            ans+=1
            i+=1
        i = 0
        while(suf[i]<=k2):
            ans+=1
            i+=1
        print(ans)


if __name__ == "__main__":
    main()
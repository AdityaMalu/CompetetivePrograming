
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
        n,q = map(int, input().split())
        s1 = list(input())
        s2 = list(input())        
        queries = []
        for i in range(q):
            queries.append(list(map(int, input().split())))
        
        for i in queries:
            i[0]-=1
            i[1]-=1

        freq_s1 = [[0] * 26 for _ in range(n + 1)]
        freq_s2 = [[0] * 26 for _ in range(n + 1)]

        for i in range(n):
            for j in range(26):
                freq_s1[i + 1][j] = freq_s1[i][j]
                freq_s2[i + 1][j] = freq_s2[i][j]
            freq_s1[i + 1][ord(s1[i]) - ord('a')] += 1
            freq_s2[i + 1][ord(s2[i]) - ord('a')] += 1

        for start, end in queries:
            diff = 0
            for j in range(26):
                count_s1 = freq_s1[end + 1][j] - freq_s1[start][j]
                count_s2 = freq_s2[end + 1][j] - freq_s2[start][j]
                diff += abs(count_s1 - count_s2)
            print(diff // 2)
    
    
    

if __name__ == "__main__":
    main()

import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import bisect
import itertools
import functools
import random

def maximize_typing_time(s):
   
    if not s:
        return "a" 

 
    time = 2 
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            time += 1
        else:
            time += 2

    max_time = time 
    max_string = s

    for pos in range(len(s) + 1):  
        for char in range(ord('a'), ord('z') + 1):  
            new_char = chr(char)
            
            
            new_s = s[:pos] + new_char + s[pos:]
            new_time = 2
            for i in range(1, len(new_s)):
                if new_s[i] == new_s[i - 1]:
                    new_time += 1
                else:
                    new_time += 2

            
            if new_time > max_time:
                max_time = new_time
                max_string = new_s

    return max_string


def main():
    t = int(input())
    for _ in range(t):
        s = (input())
        print(maximize_typing_time(s))

if __name__ == "__main__":
    main()

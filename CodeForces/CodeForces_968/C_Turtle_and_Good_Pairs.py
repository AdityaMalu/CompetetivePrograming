import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def circular_print(char_dict):
    char_list = [(char, freq) for char, freq in char_dict.items()]
    
    while char_list:
        i = 0
        while i < len(char_list):
            char, freq = char_list[i]
            print(char, end='')
            freq -= 1
            if freq == 0:
                char_list.pop(i)
            else:
                char_list[i] = (char, freq)
                i += 1

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        dict1 = {}
        for i in range(n):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
        
        circular_print(dict1)  
        print()      
            
        

if __name__ == "__main__":
    main()
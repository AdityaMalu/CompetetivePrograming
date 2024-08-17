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
        al,ar = map(int, input().split())
        bl,br = map(int, input().split())
        
        if al > bl:
            al,ar,bl,br = bl,br,al,ar
        

        if(ar < bl):
            print(1)
        else:
            if (al == bl) and (ar == br):
                print(ar-al)
            else:
                if (al == bl) or (ar == br):
                        print(min(ar-al , br-bl) + 1) 
                else:
                    if al < bl and ar > br:
                        print(br-bl+2)
                    else:
                        print(ar-bl+2)
                    

                
        

if __name__ == "__main__":
    main()
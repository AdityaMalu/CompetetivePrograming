import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def min_final_length(S):
    import re

    back_count = len(re.findall('(?=(back))', S))
    front_count = len(re.findall('(?=(front))', S))

    initial_length = len(S)

    final_length = initial_length - (front_count * 4 + back_count * 3)

    return final_length

# Example usage
S = "frontbackfrontbackfrontback"
print(min_final_length(S))


def main():
    t = int(input())
    for _ in range(t):
        # Write your code here
        S = input()
        print(min_final_length(S))

if __name__ == "__main__":
    main()
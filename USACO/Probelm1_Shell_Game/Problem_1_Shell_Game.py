import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    n = int(input())
    swaps_and_guesses = []
    for i in range(n):
        a, b, g = map(int, input().split())
        swaps_and_guesses.append((a, b, g))
    
    max_score = 0
    
    for initial_position in range(1, 4):
        current_position = initial_position
        score = 0
        
        for a, b, g in swaps_and_guesses:
            if current_position == a:
                current_position = b
            elif current_position == b:
                current_position = a
            
            if current_position == g:
                score += 1
        
        max_score = max(max_score, score)
    
    print(max_score)

def run_test(input_file, expected_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = fin
        sys.stdout = fout
        
        try:
            main()  # Run the main function
        finally:
            # Restore stdin and stdout
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    # Compare output with the expected output
    with open(expected_file, 'r') as ef, open(output_file, 'r') as of:
        expected = ef.read().strip()
        output = of.read().strip()
        
        if expected == output:
            return True
        else:
            print(f"Test failed for {input_file}")
            print(f"Expected: {expected}")
            print(f"Got: {output}")
            return False

def run_all_tests(num_tests):
    passed = 0
    for i in range(1, num_tests + 1):
        input_file = f'{i}.in'
        expected_file = f'{i}.out'
        output_file = f'{i}.tmp.out'  # Temporary output file
        
        if run_test(input_file, expected_file, output_file):
            print(f"Test {i} passed!")
            passed += 1
        else:
            print(f"Test {i} failed.")
        
        # Optionally, remove the temporary output file
        os.remove(output_file)
    
    print(f"\n{passed}/{num_tests} tests passed.")

if __name__ == "__main__":
    run_all_tests(10)

from itertools import combinations

def calculate_f(subsequence):
    return sum(subsequence[i] + subsequence[i+1] for i in range(len(subsequence) - 1))

def max_subsequence_sum(arr, k):
    max_sum = float('-inf')
    
    for subsequence in combinations(arr, k):
        max_sum = max(max_sum, calculate_f(subsequence))
    
    return max_sum

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    A = list(map(int, input().split()))
    
    result = max_subsequence_sum(A, K)
    print(result)
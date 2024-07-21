from itertools import permutations

def is_valid_permutation(arr):
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) % i != 0:
            return False
    return True

def rearrange_array(arr):
    for perm in permutations(arr):
        if is_valid_permutation(perm):
            return list(perm)
    return None

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = rearrange_array(arr)
    print(*result)
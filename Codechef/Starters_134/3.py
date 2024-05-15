#partial correct - TLE on last test case

import math
def b(arr):
    return sum(arr[:len(arr)//2+1]) - sum(arr[len(arr)//2+1:])
for _ in range(int(input())):
    n,q = map(int, input().split())
    b_arr = list(map(int, input().split()))
    a_arr = list(map(int, input().split()))
    ans = []
    for i in range(q):
        ans.append(b(sorted(b_arr[:a_arr[i]],reverse=True)))
    print(*ans)

    

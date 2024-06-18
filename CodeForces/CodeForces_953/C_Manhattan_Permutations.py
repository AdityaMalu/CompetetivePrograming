def find_permutation(n, k):
    A = list(range(1, n + 1))
    
    max_diff = sum((n - i) for i in range(n))
    
    if k > max_diff or k < 0:
        return []
    P = A[:]
    
    current_diff_sum = 0
    
    left = 0
    right = n - 1
    
    while current_diff_sum < k and left < right:
        max_possible_swap_diff = (right - left)
        
        if current_diff_sum + max_possible_swap_diff <= k:
            P[left], P[right] = P[right], P[left]
            current_diff_sum += max_possible_swap_diff
            left += 1
            right -= 1
        else:
    
            required_diff = k - current_diff_sum
            swap_index = left + required_diff
            P[left], P[swap_index] = P[swap_index], P[left]
            current_diff_sum += required_diff
            break
    
    return P
for _ in range(int(input())):
    n, k = map(int, input().split())
    permutation = find_permutation(n, k//2)
    if permutation:
        if n%2 == 0:
            maxi = ((n//2)**2)*2
        else:
            maxi = (n//2)*(n//2 + 1)*2
        if k %2 ==1 or k > maxi:
            print("NO") 
        else:
            print("YES")
            print(*permutation)
    else:
        print("NO")
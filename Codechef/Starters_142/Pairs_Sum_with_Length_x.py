def count_digit_pairs(arr, X):
    N = len(arr)
    total_count = 0
    
    digit_counts = [0] * (2 * max(arr) + 1)
    for sum_val in range(len(digit_counts)):
        digit_counts[sum_val] = len(str(sum_val))
    
    for i in range(N):
        count = [0] * (N - i)
        for j in range(i + 1, N):
            sum_ij = arr[i] + arr[j]
            if digit_counts[sum_ij] == X:
                count[j - i - 1] = 1
        
        for j in range(1, len(count)):
            count[j] += count[j - 1]
        
        total_count += sum(count)
    
    return total_count


for _ in range(int(input())):
    n, X = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_digit_pairs(arr, X))
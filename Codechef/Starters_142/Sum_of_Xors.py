def calculate_min_ugliness_sum(N, M):
    total_cells = N * M
    min_ugliness_sum = 0
    
    for K in range(1, total_cells + 1):
        # For K <= N or K <= M, it is straightforward.
        if K <= min(N, M):
            min_ugliness_sum += 2
        else:
            # For larger K, we distribute ones more evenly
            if K % 2 == 0:
                min_ugliness_sum += 2
            else:
                min_ugliness_sum += 3
    
    return min_ugliness_sum

# Input Reading
T = int(input().strip())
results = []

for _ in range(T):
    N, M = map(int, input().strip().split())
    result = calculate_min_ugliness_sum(N, M)
    results.append(result)

# Output Results
for result in results:
    print(result)

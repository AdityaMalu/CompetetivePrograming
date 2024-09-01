def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        max_sum = float('-inf')
        min_operations = 0

        if (max(arr) < 0):
            print(0)
            continue
        
        for i in range(n):
            for j in range(i, n):
                current_sum = 0
                operations = 0
                for k in range(i, j + 1):
                    if arr[k] < 0:
                        operations += 1
                    current_sum += max(arr[k], 0)
                
                if current_sum > max_sum:
                    max_sum = current_sum
                    min_operations = operations
                elif current_sum == max_sum:
                    min_operations = min(min_operations, operations)
        
        print(min_operations)

if __name__ == "__main__":
    main()
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        arr = list(map(int, data[index:index + n]))
        index += n
        
        arr.sort()
        
        max_sum = 0
        current_sum = 0
        start = 0
        
        for end in range(n):
            current_sum += arr[end]
            while current_sum > m or arr[end] - arr[start] > 1:
                current_sum -= arr[start]
                start += 1
            max_sum = max(max_sum, current_sum)
        
        results.append(max_sum)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()

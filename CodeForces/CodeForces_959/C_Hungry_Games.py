def main():
    import bisect
    
    for _ in range(int(input())):
        n, s = map(int, input().split())
        arr = list(map(int, input().split()))
        
        ps = [0] * (n + 1)
        dp = [0] * (n + 3)
        total = 0
        
        for i in range(n):
            ps[i + 1] = ps[i] + arr[i]
        
        for i in range(n - 1, -1, -1):
            req_sum = ps[i] + s
            lb = bisect.bisect_left(ps, req_sum, i + 1, n + 1)
            
            if lb == (n + 1):
                dp[i] += (n - i)
            elif req_sum == ps[lb]:
                dp[i] += (lb - i) + dp[lb + 1]
            else:
                dp[i] += (lb - i - 1) + dp[lb]
        
        total = sum(dp[:n + 2])
        print(total)

if __name__ == "__main__":
    main()

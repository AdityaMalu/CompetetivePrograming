def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input().strip()
        
        cnt = 0
        init = 0
        
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                init += 1
        
        temp = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                temp += 1
            else:
                cnt += (temp - 1)
                temp = 1
        
        if temp > 0:
            cnt += (temp - 1)
        
        ans = 0
        ans += cnt * init
        n -= cnt
        ans += ((n - 2) * (n - 1)) // 2
        
        print(ans)

if __name__ == "__main__":
    solve()

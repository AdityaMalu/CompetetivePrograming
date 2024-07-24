def solve():
    n = int(input())
    a = []

    for i in range(n):
        row = list(map(int, list(input().strip())))
        a.append(row)

    ans = 0

    for i in range((n + 1) // 2):
        for j in range(n // 2):
            nowi, nowj = i, j
            sum_vals = a[nowi][nowj]

            nowi, nowj = nowj, n - nowi - 1
            sum_vals += a[nowi][nowj]

            nowi, nowj = nowj, n - nowi - 1
            sum_vals += a[nowi][nowj]

            nowi, nowj = nowj, n - nowi - 1
            sum_vals += a[nowi][nowj]

            ans += min(sum_vals, 4 - sum_vals)

    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

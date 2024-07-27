def query(l, r, p):
    return p[r] - (p[l - 1] if l > 0 else 0)

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    p = [0] * n
    for i in range(n):
        p[i] = a[i] + (p[i - 1] if i > 0 else 0)

    ans = float('inf')

    for i in range(n):
        l, r, pos = i, n - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if query(i, mid, p) <= s:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        if pos == -1 or query(i, pos, p) != s:
            continue
        ans = min(ans, n - (pos - i + 1))

    print(-1 if ans == float('inf') else ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

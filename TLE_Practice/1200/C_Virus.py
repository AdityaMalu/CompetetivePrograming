def solve_case(n, m, a):
    a.sort()
    gaps = []

    for i in range(1, m):
        gaps.append(a[i] - a[i - 1] - 1)
    
    gap = a[0] + n - a[-1] - 1
    if gap > 0:
        gaps.append(gap)

    gaps.sort(reverse=True)
    ans = 0
    cnt = 0

    for gap in gaps:
        if gap - cnt * 2 > 0:
            ans += max(1, gap - cnt * 2 - 1)
        cnt += 2

    return n - ans

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0

    T = int(data[idx])
    idx += 1
    results = []

    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + m]))
        idx += m
        results.append(solve_case(n, m, a))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()

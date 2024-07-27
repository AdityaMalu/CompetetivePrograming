def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        if any(v[i - 1] > 1 and v[i] == 1 for i in range(1, n)):
            print("-1")
            continue
        
        ops = [0] * n

        for i in range(1, n):
            him = v[i - 1]
            me = v[i]
            extra = 0
            while him != 1 and him * him <= me:
                extra -= 1
                him *= him
            while me < him:
                extra += 1
                me *= me

            ops[i] = max(0, ops[i - 1] + extra)

        ans = sum(ops)
        print(ans)

if __name__ == "__main__":
    solve()

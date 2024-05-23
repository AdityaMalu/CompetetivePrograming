# Post Contest

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    maxn = 1
    for i in range(20):
        mz = 0
        run = 0
        for j in range(n):
            x = a[j]
            if (x >> i) % 2 == 1:
                run = 0
            else:
                run += 1
            mz = max(mz, run)
        
        if mz < n:
            maxn = max(maxn, mz + 1)

    print(maxn)

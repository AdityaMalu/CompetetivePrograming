#problem: https://codeforces.com/contest/1976/problem/C

#postcontest

def solution():
    def f(n, m):
        total = 0
        for i in range(n+m):
            if (a[i] > b[i] and n) or (a[i] < b[i] and not m):
                total += a[i]
                n -= 1
            else:
                total += b[i]
                m -= 1
        return total
        
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total1, total2 = f(n+1, m), f(n, m+1)
    n += 1
    result = [0]*(n+m)
    for i in range(n+m):
        if (a[i] > b[i] and n) or (a[i] < b[i] and not m):
            result[i] = total1-a[i]
            n -= 1
        else:
            result[i] = total2-b[i]
            m -= 1
    return " ".join(map(str, result))

for _ in range(int(input())):
    print(solution())

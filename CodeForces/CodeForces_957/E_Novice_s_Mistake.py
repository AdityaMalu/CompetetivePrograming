

def solve():
    n = input()
    ans = []
    for i in range(1, 10001):
        s = n * i
        len_s = len(s)
        for j in range(1, min(i, 6)):
            if int(s[: j]) == i * int(n) - (len_s - j):
                ans.append((i, len_s - j))
    print(len(ans))
    for i in ans:
        print(*i)

for _ in range(int(input())):
    solve()
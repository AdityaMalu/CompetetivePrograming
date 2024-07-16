def solve():
    n = int(input())
    ans = [n]
    
    if n == 1:
        print(1)
        print(1)
        return
    
    k = 0
    mp1 = {}
    for i in range(61):
        if n & (1 << i):
            mp1[k] = i
            k += 1
    
    for i in range(k):
        x = 0
        for j in range(61):
            if ((1 << k) - 1 - (1 << i)) & (1 << j):
                x += (1 << mp1[j])
        if x != 0:
            ans.append(x)
    
    print(len(ans))
    print(*reversed(ans))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
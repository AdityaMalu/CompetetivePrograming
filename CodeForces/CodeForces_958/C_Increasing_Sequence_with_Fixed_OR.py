def solve():
    n = int(input().strip())
    ans = [n]
    
    bitw = 1
    while bitw < n:
        if(n & bitw):
            ans.append(n - bitw)
        bitw <<= 1
    
    print(len(ans))
    print(*sorted(ans))
        

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
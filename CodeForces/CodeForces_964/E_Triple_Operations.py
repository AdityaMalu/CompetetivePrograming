import sys
import math

M = 10**9 + 7

def log3(a, b):
    return math.log2(a) / math.log2(b)

def main():
    T = int(input())
    for _ in range(T):
        l, r = map(int, input().split())
        
        dn = int(log3(l, 3)) + 1
        up = int(log3(r, 3)) + 1
        ans = dn
        
        n2 = l
        while dn < up:
            n1 = pow(3, dn)
            ans += (n1 - n2) * dn
            dn += 1
            n2 = n1
        
        ans += (r - n2 + 1) * dn
        print(ans)
if __name__ == "__main__":
    main()

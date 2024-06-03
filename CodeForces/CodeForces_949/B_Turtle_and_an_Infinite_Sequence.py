#https://codeforces.com/contest/1981/problem/B
#post contest

for _ in range(int(input())):
    a,b = map(int, input().split())
    ans = 0
    l = max(0,a-b)
    r = a+b
    for i in range(32):
        c = r//(1<<i)
        if(c%2!=0):
            ans|=1<<i
            continue
        if(l==0):
            if(c):
                ans|=1<<i
        c2 = l//(1<<i)
        if(c!=c2):
            ans|=1<<i
    print(ans)



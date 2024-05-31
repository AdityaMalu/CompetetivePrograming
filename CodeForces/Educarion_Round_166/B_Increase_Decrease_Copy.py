# Link: https://codeforces.com/contest/1976/problem/B
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    ans = 0
    flag = False
    temp = 10**9+1

    for i in range(n):
        ans+= abs(a[i]-b[i])
    for i in range(n):
        if a[i]>b[i]:
            if b[i]<=b[-1]<=a[i]:
                flag = True
            temp = min(temp,abs(b[-1]-a[i]),abs(b[-1]-b[i]))
        elif a[i]<b[i]:
                if a[i]<=b[-1]<=b[i]:
                    flag = True
                temp = min(temp,abs(b[-1]-a[i]),abs(b[-1]-b[i]))
        else:
            if (a[i] == b[i] == b[-1]):
                flag = True
            temp = min(temp,abs(a[i] - b[-1]))
    ans+=1
    if  not flag:
        ans+=temp

    print(ans)
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    ans = 0
    if (a+b+c) % 2 == 1:
        print(-1)
    else:
        while(a>0):
            if b >= c:
                b-=1
            else:
                c-=1
            ans+=1
            a-=1
        print(ans + min(b,c))
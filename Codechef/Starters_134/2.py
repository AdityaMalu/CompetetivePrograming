for _ in range(int(input())):
    n = int(input())
    div = n//9
    rem  = n%9
    ans = div*45 + (rem*(rem+1))//2
    print(ans)
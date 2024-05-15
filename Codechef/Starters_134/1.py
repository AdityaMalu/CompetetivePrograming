import math
for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    prev = s[0]
    count = 1
    if n == 1:
        ans = 1
    else:
        for i in range(1,n):
            if s[i] != s[i-1]:
                ans+= math.ceil(count/2)
                count = 0
            count+=1
        ans+= math.ceil(count/2)
    print(ans) 
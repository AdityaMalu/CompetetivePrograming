for _ in range(int(input())):
    n = int(input())
    s = input()
    temp1 = 0
    temp2 = 0
    for i in range(n):
        if s[i] == 'N':
            temp1+=1
        elif s[i] == 'S':
            temp1-=1
        elif s[i] == 'E':
            temp2+=1
        else:
            temp2-=1
    if temp1%2==0 and temp2%2 == 0:
        print("YES")
    else:
        print("NO")

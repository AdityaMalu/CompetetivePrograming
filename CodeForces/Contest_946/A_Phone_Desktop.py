import math
for _ in range(int(input())):
    a,b = map(int, input().split())
    div = math.ceil(b/2)
    rem = div*15-b*4
    a-=rem
    if a<=0:
        print(div)
    else:
        print(div+(a+14)//15)


        





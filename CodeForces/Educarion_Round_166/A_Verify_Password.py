# Link: https://codeforces.com/contest/1976/problem/A

for _  in range(int(input())):
    n = int(input())
    s = input()
    ans = 'YES'
    prev = s[0]
    flag = False
    if 'a'<= prev <='z':
        flag = True
    for i in range(1,n):
            if flag == False:
                if  '0'<= prev <='9' and '0'<= s[i] <='9' and s[i]>=prev:
                    prev = s[i]
                    continue
                elif '0'<= prev <='9' and 'a'<= s[i] <='z':
                    prev = s[i]
                    flag = True
                    continue
                else:
                    ans = "NO"
                    break
            else:
                if '0'<=s[i]<='9':
                    ans = 'NO'
                    break
                else:
                    if  'a'<= prev <='z' and 'a'<= s[i] <='z' and s[i]>=prev:
                        prev = s[i]
                        continue
                    else:
                        ans = "NO"
                        break
    print(ans)


                


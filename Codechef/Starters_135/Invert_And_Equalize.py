for _ in range(int(input())):
    n = int(input())
    s = input()
    arr0 = 0
    arr1  = 0
    prev = s[0]
    for i in range(n):
        if s[i] != prev:
            if prev == '0':
                arr0+=1
            else:
                arr1+=1
            prev = s[i]
    if s[-1] == '0':
        arr0+=1
    else:
        arr1+=1
        
    print(min(arr0, arr1))
        
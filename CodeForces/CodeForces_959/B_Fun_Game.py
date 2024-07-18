def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s1 = input()
        s2 = input()
        flag = False
        flag2 = False
        for i in range(n):
            if s1[i] == '1':
                flag = True
            if s1[i] == '0' and s2[i] == '1':
                if not flag:
                    print("NO")
                    flag2 = True
                    break
        if not flag2:
            print("YES")

if __name__ == "__main__":
    main()

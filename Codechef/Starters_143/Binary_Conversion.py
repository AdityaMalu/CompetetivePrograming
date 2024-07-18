def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        str1 = input()
        str2 = input()
        
        count_one = 0
        count_zero = 0
        count_diff = 0
        initial_same_one = 0
        initial_same_zero = 0
        count_one_diff = 0
        count_zero_diff = 0
        
        for i in range(n):
            if str1[i] == '0':
                count_zero += 1
            elif str1[i] == '1':
                count_one += 1

            if str2[i] == '0':
                count_zero -= 1
            elif str2[i] == '1':
                count_one -= 1

            if str1[i] != str2[i]:
                if str1[i] == '0':
                    count_one_diff += 1
                else:
                    count_zero_diff += 1
                count_diff += 1
            else:
                if str1[i] == '0':
                    initial_same_zero += 1
                else:
                    initial_same_one += 1
        
        if count_one != 0 or count_zero != 0:
            print("NO")
            continue
        
        k -= (count_diff // 2)
        initial_same_zero += (count_diff // 2)
        initial_same_one += (count_diff // 2)
        
        if k == 0:
            print("YES")
        elif k < 0:
            print("NO")
        else:
            if initial_same_zero > 1 or initial_same_one > 1:
                print("YES")
            elif k % 2 == 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()

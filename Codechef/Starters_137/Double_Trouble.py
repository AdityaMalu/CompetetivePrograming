def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        coor = list(map(int, input().split()))
        power = list(map(int, input().split()))

        if n == 1:
            print("YES")
            continue

        i, j = 0, 0
        break1 = 0

        while i < n - 1 and coor[i + 1] <= coor[i] + power[i]:
            i += 1

        while j < n - 1 and coor[j + 1] - power[j + 1] <= coor[j]:
            j += 1

        break1 = max(i,j)+1
        if break1 == n:
            print("YES")
            continue

        
        i, j = break1, break1

      
        while i < n - 1 and coor[i + 1] <= coor[i] + power[i]:
            i += 1
    
        while j < n-1 and coor[j] >= coor[j + 1] - power[j + 1]:
            j += 1

        break2 = max(i, j)

        if break2 >= n - 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

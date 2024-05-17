def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        
        ans = [(n + 1) - x for x in a]
        
        temp = 0
        for i in range(n):
            if ans[i] == n:
                temp = i
        
        arr = [(n, temp)]
        
        for i in range(n):
            if i % 2 != temp % 2:
                arr.append((ans[i], i))
        arr.sort(reverse=True)
        
        for i in range(1, len(arr)):
            ans[arr[i][1]] = arr[i - 1][0]
        
        ans[arr[0][1]] = arr[-1][0]
        
        print(*ans)

if __name__ == "__main__":
    main()

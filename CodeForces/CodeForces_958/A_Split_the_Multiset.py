def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        cnt = 0
        if n == 1:
            print(0)
            continue
        cnt = (n - 1) // (k - 1)
        temp = (n - 1) % (k - 1)
        if temp > 1:
            cnt += 1
        else:
            cnt += temp
        print(cnt)

if __name__ == "__main__":
    main()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sum1,sum2 = 0,0
        for i in range(n):
            sum1 = max((sum1 + arr[i]) ,abs(arr[i] + sum2))
            sum2 = sum2 + arr[i]
        print(sum1)

if __name__ == "__main__":
    main()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        barr = input()

        pre_sum_a = [0] * (n + 1)

        for i in range(n):
            pre_sum_a[i + 1] = pre_sum_a[i] + arr[i]

        ans = 0
        k, j = 0, n - 1
        
        while k < j:
            if barr[k] == 'L' and barr[j] == 'R':
                ans += pre_sum_a[j + 1] - pre_sum_a[k]
                k += 1
                j -= 1
            elif barr[k] == 'R':
                k += 1
            elif barr[j] == 'L':
                j -= 1

        print(ans)

if __name__ == "__main__":
    main()

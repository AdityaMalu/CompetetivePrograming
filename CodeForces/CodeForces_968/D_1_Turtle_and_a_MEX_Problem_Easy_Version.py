def main():
    tes = int(input())
    results = []

    for _ in range(tes):
        que, m = map(int, input().split())
        max_val = 0

        for _ in range(que):
            a = list(map(int, input().split()))
            set_a = set(a)

            first = 0
            while True:
                if first not in set_a:
                    set_a.add(first)
                    break
                first += 1
                

            while True:
                if first not in set_a:
                    max_val = max(max_val, first)
                    break
                first += 1

        if m >= max_val:
            ans = max_val * (max_val + 1)
            big = (m * (m + 1)) // 2 - ans // 2
            results.append(ans + big)
        else:
            ans = max_val * (m + 1)
            results.append(ans)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
def solve():
    n, budget = map(int, input().split())

    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    pq_map = {p[i]: q[i] for i in range(n)}

    max_profit = 0
    for price in sorted(pq_map.keys()):
        curr_qty = pq_map[price]
        next_qty = pq_map.get(price + 1, 0)

        buy = min(curr_qty, budget // price)
        rem = budget - buy * price
        next = min(next_qty, rem // (price + 1))
        rem -= next * (price + 1)

        max_profit = max(max_profit, buy * price + next * (price + 1))

        left_next = next_qty - next
        left_budget = rem
        adjust = min(min(buy, left_budget), left_next)
        buy -= adjust
        next += adjust

        max_profit = max(max_profit, buy * price + next * (price + 1))

    print(max_profit)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()

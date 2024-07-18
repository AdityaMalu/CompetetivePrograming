def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    pref = [0] * (n + 1)
    prefmax = [0] * n
    
    prefmax[0] = arr[0]
    pref[1] = arr[0]
    
    for i in range(1, n):
        pref[i + 1] = pref[i] + arr[i]
        prefmax[i] = max(prefmax[i - 1], arr[i])

    queries = list(map(int, input().split()))
    
    results = []
    for k in queries:
        ind = next((i for i, val in enumerate(prefmax) if val > k), n)
        results.append(pref[ind])
    
    print(" ".join(map(str, results)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

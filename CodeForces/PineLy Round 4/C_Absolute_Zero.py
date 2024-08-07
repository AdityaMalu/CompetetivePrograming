def solve_case(n, arr):
    operations = []
    
    while max(arr) > 0:
        if len(operations) >= 40:
            return [-1]  

        non_zero = [x for x in arr if x != 0]
        if len(non_zero) > 1 and (non_zero[0] % 2) != (non_zero[1] % 2):
            return [-1]  

        mini = min(arr)
        maxi = max(arr)
        x = (mini + maxi) // 2
        operations.append(x)
        arr = [abs(a - x) for a in arr]
    
    r = [len(operations)] + operations
    return r

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        r = solve_case(n, arr)
        if r[0] == -1:
            print(-1)
        else:
            print(r[0])
            print(" ".join(map(str, r[1:])))

if __name__ == "__main__":
    main()

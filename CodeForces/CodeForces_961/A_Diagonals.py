def min_diagonals(n, k):
    diagonals = []
    
    # First n diagonals
    for i in range(1, n + 1):
        diagonals.append(i)
    
    # Last n-1 diagonals
    for i in range(n - 1, 0, -1):
        diagonals.append(i)
    
    diagonals.sort(reverse=True)
    
    total_cells = 0
    num_diagonals = 0
    
    for diagonal in diagonals:
        total_cells += diagonal
        num_diagonals += 1
        if total_cells >= k:
            return num_diagonals
    
    return num_diagonals

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if k == 0:
            print(0)
            continue
        print(min_diagonals(n, k))

if __name__ == "__main__":
    main()


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        x = int(data[index + 1])
        y = int(data[index + 2])
        index += 3
        
        arr = [0] * (n + 1)
        ind = -1
        
        for i in range(y - 1, 0, -1):
            arr[i] = ind
            ind *= -1
        
        for i in range(y, x + 1):
            arr[i] = 1
        
        ind = -1
        for i in range(x + 1, n + 1):
            arr[i] = ind
            ind *= -1
        
        results.append(arr[1:])
    
    for result in results:
        print(*result)

if __name__ == "__main__":
    main()

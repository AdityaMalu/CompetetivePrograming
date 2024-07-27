def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    M = 10**9 + 7
    
    results = []
    for _ in range(T):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        from collections import Counter
        
        ump = Counter(a)
        dict1 = list(ump.values())
        dict1.sort(reverse=True)
        
        ans = 0
        result = float('-inf')
        for i in range(1, len(dict1) + 1):
            ans += dict1[i - 1]
            v1 = (ans // i) * i
            result = max(result, v1)
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
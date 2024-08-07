def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        p = list(map(int, data[index:index + n - 1]))
        index += n - 1
        
        from collections import defaultdict, deque
        
        tree = defaultdict(list)
        for i in range(n - 1):
            tree[p[i] - 1].append(i + 1)
        
        def dfs(node):
            max_value = a[node]
            for child in tree[node]:
                max_value += dfs(child)
            return max_value
        
        results.append(dfs(0))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()


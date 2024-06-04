# https://codeforces.com/contest/1980/problem/C


from collections import defaultdict, Counter

def main():
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
        b = list(map(int, data[index:index + n]))
        index += n
        m = int(data[index])
        index += 1
        d = list(map(int, data[index:index + m]))
        index += m

        if d[-1] not in b:
            results.append("NO")
            continue

        diff_count = Counter(b[i] for i in range(n) if a[i] != b[i])
        d_count = Counter(d)
        
        is_possible = True
        for num, cnt in diff_count.items():
            if cnt > d_count[num]:
                is_possible = False
                break
        
        if is_possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

# https://codeforces.com/contest/1980/problem/E

#post contest

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
        m = int(data[index + 1])
        index += 2
        
        r = {}
        c = {}
        
        matrix1 = []
        for i in range(n):
            row = list(map(int, data[index:index + m]))
            index += m
            matrix1.append(row)
        
        matrix2 = []
        for i in range(n):
            row = list(map(int, data[index:index + m]))
            index += m
            matrix2.append(row)
        
        for i in range(n):
            for j in range(m):
                a = matrix1[i][j]
                r[a] = i + 1
                c[a] = j + 1
        
        cnt1 = {}
        cnt2 = {}
    
        for i in range(n):
            for j in range(m):
                a = matrix2[i][j]
                if r[a] != i + 1:
                    if (r[a], i + 1) not in cnt1:
                        cnt1[(r[a], i + 1)] = 0
                    cnt1[(r[a], i + 1)] += 1
                if c[a] != j + 1:
                    if (c[a], j + 1) not in cnt2:
                        cnt2[(c[a], j + 1)] = 0
                    cnt2[(c[a], j + 1)] += 1
        
        ans = True
        
        for value in cnt2.values():
            if value != n:
                ans = False
                break
        
        if ans:
            for value in cnt1.values():
                if value != m:
                    ans = False
                    break
        


        if ans:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

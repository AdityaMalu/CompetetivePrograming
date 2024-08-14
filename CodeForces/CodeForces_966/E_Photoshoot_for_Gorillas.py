def cal_freq(m, n, k):
    freq_list = [0] * (m * n)
    
    for i in range(m):
        for j in range(n):
            top = max(0, i - k + 1)
            left = max(0, j - k + 1)
            bottom = min(m - k + 1, i + 1)
            right = min(n - k + 1, j + 1)
            freq = (bottom - top) * (right - left)
            freq_list[i * n + j] = freq
    
    return sorted(freq_list, reverse=True)

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        no = int(input())
        arr = sorted(map(int, input().split()), reverse=True)
        
        freq_arr = cal_freq(m, n, k)
        
        ans = sum(arr[i] * freq_arr[i] for i in range(no))
        
        print(ans)

if __name__ == "__main__":
    main()
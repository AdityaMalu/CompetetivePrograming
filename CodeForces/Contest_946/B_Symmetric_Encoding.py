for _ in range(int(input())):
    n = int(input())
    s = input()
    arr = sorted(set(s))
    dict1 = {}

    half_len = len(arr) // 2
    for i in range(half_len):
        dict1[arr[i]] = arr[-(i + 1)]
        dict1[arr[-(i + 1)]] = arr[i]
    
    if len(arr) % 2 != 0:
        dict1[arr[half_len]] = arr[half_len]

    ans = ''.join(dict1[char] for char in s)
    print(ans)

t = int(input())
for T in range(t):
	n, l, r = map(int, input().split())
	a = [int(x) for x in input().split()]
	ans = 0
	cur = 0
	L, R = 0, 0
	while L < n:
		while R < n and cur < l:
			cur += a[R]
			R += 1
		if l <= cur and cur <= r:
			ans += 1
			L = R
			cur = 0
		else:
			cur -= a[L]
			L += 1
	print(ans)
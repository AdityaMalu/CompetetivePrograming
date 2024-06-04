# https://codeforces.com/contest/1980/problem/D

#post contest
import math
def gcd(x, y):
    return math.gcd(x, y)


def is_non_decreasing(a,temp):

    arr = []
    for i in range(len(a)):
        if i == temp:
            continue
        arr.append(a[i])

    last = 1
    for i in range(1,len(arr)):
        y = gcd(arr[i-1], arr[i])
        if y < last:
            return False
        last = y
    return True
    

def possible_to_remove_one(a):
    n = len(a)
    b = [gcd(a[i], a[i+1]) for i in range(n-1)]
     
    temp = -1
    for i in range(n-2):
        if b[i]>b[i+1]:
            temp = i
            break
    
    if is_non_decreasing(a,temp) or is_non_decreasing(a,temp+1) or is_non_decreasing(a,temp+2):
        return True
    
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        if possible_to_remove_one(a):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

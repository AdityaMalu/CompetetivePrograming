def solve_case(nums):
    n = len(nums)
    ans = n * (n + 1) // 2  
    
    for x in [1, 2, 3]:
        dont_want = x - 1 if x > 1 else 3
        
        left, right = float('inf'), -1
        will_replace = False
        
        for i in range(n):
            if nums[i] == x:
                left = min(left, i)
                right = max(right, i)
        
        if left == float('inf'):
            continue 
        
        for i in range(left, right):
            if nums[i] == dont_want:
                will_replace = True
                break
        
        if not will_replace:
            l2 = left
            r2 = right
            
            while l2 >= 0 and nums[l2] != dont_want:
                l2 -= 1
            while r2 < n and nums[r2] != dont_want:
                r2 += 1
            
            ans -= (left - l2) * (r2 - right)
    
    return ans

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        
        result = solve_case(nums)
        print(result)

if __name__ == "__main__":
    main()

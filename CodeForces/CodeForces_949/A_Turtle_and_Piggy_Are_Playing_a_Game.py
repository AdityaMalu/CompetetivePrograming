import math

def largest_power_of_two_in_range(a, b):
    if a > b:
        return -1
    largest_power = 1 << (b.bit_length() - 1)
    
    if largest_power < a:
        largest_power >>= 1
    return largest_power

for _ in range(int(input())):
    a, b = map(int, input().split())
    largest_power = largest_power_of_two_in_range(a, b)
    if largest_power >= a and largest_power <= b:
        ans = math.log2(largest_power)
    print(int(ans))
   


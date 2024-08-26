import heapq
from collections import defaultdict

MOD = 10**9 + 7

def main():
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        # Count the frequency of each number and initialize the heap
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1

        # Create a min-heap of the unique numbers
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        total_sum = sum(A)

        while K > 0 and min_heap:
            min_val = heapq.heappop(min_heap)
            current_freq = freq[min_val]

            if current_freq <= K:
                K -= current_freq
                total_sum += min_val * current_freq

                # Merge the values into min_val * 2
                next_val = min_val * 2
                freq[next_val] += current_freq
                if freq[next_val] == current_freq:
                    heapq.heappush(min_heap, next_val)
                freq[min_val] = 0
            else:
                total_sum += min_val * K
                freq[min_val] -= K
                next_val = min_val * 2
                freq[next_val] += K
                heapq.heappush(min_heap, min_val)
                K = 0

        result_sum = total_sum % MOD
        print(result_sum)

if __name__ == "__main__":
    main()

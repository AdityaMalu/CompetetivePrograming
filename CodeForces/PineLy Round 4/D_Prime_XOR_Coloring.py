import sys
from collections import defaultdict
import itertools

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(max_num + 1) if is_prime[p]]
    return primes, is_prime

def construct_graph(n, is_prime):
    adjacency_list = {i: [] for i in range(1, n + 1)}
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if is_prime[u ^ v]:
                adjacency_list[u].append(v)
                adjacency_list[v].append(u)
    return adjacency_list

def greedy_coloring(graph, n):
    result = [-1] * (n + 1)
    available_colors = [True] * (n + 1)
    result[1] = 0

    for u in range(2, n + 1):
        for v in graph[u]:
            if result[v] != -1:
                available_colors[result[v]] = False

        color = next(color for color, available in enumerate(available_colors) if available)
        result[u] = color

        for v in graph[u]:
            if result[v] != -1:
                available_colors[result[v]] = True

    return max(result) + 1, result[1:]

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        max_prime_check = 2 * n - 1
        primes, is_prime = sieve_of_eratosthenes(max_prime_check)
        graph = construct_graph(n, is_prime)
        num_colors, node_colors = greedy_coloring(graph, n)
        results.append(f"{num_colors}")
        results.append(" ".join(str(x + 1) for x in node_colors))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

def solution(N, A):
    counters = [0] * N
    max_counter = 0

    for X in A:
        if 1 <= X <= N:
            counters[X-1] += 1
            max_counter = max(max_counter, counters[X-1])
        elif X == N + 1:
            counters = [max_counter] * N

    return counters


A = [3, 4, 4, 6, 1, 4, 4]
N = 5

print(solution(N, A))  # expected output  [3, 2, 2, 4, 2]

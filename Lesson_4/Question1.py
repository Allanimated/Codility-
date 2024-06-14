def solution(X, A):
    covered_positions = set()
    for time, position in enumerate(A):
        if position <= X:
            covered_positions.add(position)
        if len(covered_positions) == X:
            return time
    return -1


# Example usage:
X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))  # Output: 6

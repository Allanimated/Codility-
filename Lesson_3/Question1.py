def solution(X, Y, D):
    import math
    distance = Y - X
    jumps = math.ceil(distance // D)
    return jumps


# Example usage:
X = 10
Y = 85
D = 30
print(solution(X, Y, D))  # Output: 3

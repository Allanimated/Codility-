def solution(A):
    n = len(A)
    total_sum = (n + 1) * (n + 2) // 2  # Sum of integers from 1 to (N + 1)
    array_sum = sum(A)
    missing_element = total_sum - array_sum
    return missing_element


# Example usage:
A = [2, 3, 1, 5]
print(solution(A))  # Output: 4

def solution(A):
    unpaired_element = 0

    # XOR all elements of the array
    for num in A:
        unpaired_element ^= num

    return unpaired_element


# Example usage:
A = [9, 3, 9, 8, 9, 7, 9, 7, 8]
print(solution(A))  # Output: 7

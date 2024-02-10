def solution(N):
    binary = (bin(N))[2:]
    binary_gap = 0
    track = list()

    for index in range(len(binary)):
        if binary[index] == "1":
            track.append(index)
        pass

    for i in range(len(track)-1):
        zero_count = (track[i+1] - track[i])-1
        if zero_count > binary_gap:
            binary_gap = zero_count
    return binary_gap


# Test cases
print(solution(1041))  # Output: 5
print(solution(32))    # Output: 0

# ChatGPT's Solution


def solution_chatGPT(N):
    # Convert integer N to binary representation
    binary_str = bin(N)[2:]

    # Initialize variables to track the longest binary gap and the current binary gap length
    max_gap_length = 0
    current_gap_length = 0

    # Iterate through the binary string
    for digit in binary_str:
        if digit == '0':
            # Increment current gap length if the current digit is '0'
            current_gap_length += 1
        else:
            # Update max gap length if the current gap is greater
            max_gap_length = max(max_gap_length, current_gap_length)
            # Reset current gap length
            current_gap_length = 0

    return max_gap_length


# Test cases
print(solution_chatGPT(1041))  # Output: 5
print(solution_chatGPT(32))    # Output: 0

from typing import List


def longest_sequence(X: List[int]) -> int:
    count = -1
    if len(X) == 1:
        return 0
    if len(X) > 1:
        current_longest_subsequence = 0
        count = 1
        for i in range(0, len(X)-1):
            adjacent_element = X[i + 1]
            if X[i] ^ X[i + 1] == 1:
                count+=1
                current_longest_subsequence=count
            else:
                if count > current_longest_subsequence and count != 1:
                    current_longest_subsequence=count
                count = 1
        return current_longest_subsequence
    
    return count

print(longest_sequence([0,0,1,1,0,1]))
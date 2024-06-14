def solution(A: list) -> int:
    """
    1. start by looking for the smallest missing number which is 1
    2. have a track of seen numbers
    3. Add any number thats not what you are looking for  in cache
    4. if you find the smallest number move to the next smallest number after it
    look up O(1)
    iteration O(n)
    """
    # Set lowest possible value greater than 0
    smallest_positive_int = 1
    # Keep a track of seen numbers
    seen = set()
    # Start at pointer at 0
    i = 0
    while i < len(A):
        if A[i] == smallest_positive_int:
            # Move to the next smallest value
            smallest_positive_int += 1
        elif A[i] != smallest_positive_int and A[i] not in seen:
            # keep a track
            seen.add(A[i])

        i += 1

    j = 0
    while j < len(seen):
        if smallest_positive_int in seen:
            smallest_positive_int += 1

        j += 1

    return smallest_positive_int


A = [1, 3, 6, 4, 5, 2]

print(solution(A))

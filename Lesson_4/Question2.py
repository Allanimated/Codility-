
def solution(A):
    n = len(A)
    if n != len(set(A)) or min(A) != 1 or max(A) != n:
        return 0
    return 1

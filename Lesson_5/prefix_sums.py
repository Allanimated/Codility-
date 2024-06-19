from typing import List


A = [2, 3, 7, 5, 1, 3, 9]


def prefix_sums(A: List[int]) -> List[int]:
    n: int = len(A)
    P: List[int] = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P: List[int], x: int, y: int) -> int:
    return P[y + 1] - P[x]


def mushrooms(A: List[int], k: int, m: int) -> int:
    """
        A: An array that represents number of mushrooms growing on the
        consecutive spots along a road
        k: The initial position of the mushroom picker
        m: Number of moves made by the picker
    """
    n: int = len(A)
    result = 0
    pref: List[int] = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + (m - 2 * p)))
        result: int = max(result, count_total(pref, left_pos, right_pos))
    print("result from first loop;",result)
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result: int = max(result, count_total(pref, left_pos, right_pos))
    return result


# print(count_total(P=prefix_sums(A), x=2, y=2))
print(mushrooms(A=A, k=4, m=2))
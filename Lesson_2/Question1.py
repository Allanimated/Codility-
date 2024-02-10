def solution(arr, k):
    for _ in range(k):
        last_elem = arr.pop()
        arr.insert(0, last_elem)

    print(arr)


solution([3, 8, 9, 7, 6], 6)

def binary_search(A, n, k):
    # 探索範囲 [left, right]
    left, right = -1, n

    # 探索範囲を狭めていく
    while right - left > 1:

        # 探索範囲の中央
        mid = (left + right) // 2

        if is_ok(A[mid], k):
            right = mid
        else:
            left = mid

    return right

def is_ok(target, k):
    return target > k

n = int(input())
A = list(map(int,input().split()))
A.sort()
q = int(input())
for i in range(q):
    k = int(input())
    print(n - binary_search(A, n, k))

n = int(input())
A = list(map(int, input().split()))

# bubble_sort(A : 配列, n : Aの要素数)
#     for i = 0 to n-2
#         for j = n-1 down to i+1
#             if a[j-1] > a[j] then
#                 swap(a[j-1], a[j])

for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if A[j-1] > A[j]:
            A[j-1],A[j] = A[j],A[j-1]
    print(*A)

n = int(input())
A = list(map(int, input().split()))

for i in range(0, n-1):
    min_index = i
    for j in range(i+1, n):
        if A[j] < A[min_index]:
            min_index = j
    A[i],A[min_index] = A[min_index],A[i]
    print(*A)

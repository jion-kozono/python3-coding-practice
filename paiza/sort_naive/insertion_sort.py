n = int(input())
A = list(map(int, input().split()))

for i in range(1, n):
    x = A[i]
    j = i-1
    while j >= 0 and A[j] > x:
        A[j+1] = A[j]
        j-=1
    A[j+1] = x
    print(*A)

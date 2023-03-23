n = int(input())
A = list(map(int, input().split()))
k = int(input())

A = sorted(set(A), reverse=True)
print(A[k-1])

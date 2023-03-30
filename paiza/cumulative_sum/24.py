n, range_n = 5, 10
a = [0] * (range_n+1)
L = [0] * n
R = [0] * n

for i in range(n):
    L[i], R[i] = map(int, input().split())

for i in range(n):
    a[L[i] - 1] += 1
    a[R[i]] -= 1

for i in range(range_n):
    a[i + 1] += a[i]

print(max(a))

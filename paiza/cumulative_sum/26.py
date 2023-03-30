n, q = map(int, input().split())
a = [0] * (n+1)
L = [0] * q
R = [0] * q

for i in range(q):
    L[i], R[i] = map(int, input().split())

for i in range(q):
    a[L[i] - 1] += 1
    a[R[i]] -= 1

for i in range(n):
    a[i + 1] += a[i]

print(max(a))

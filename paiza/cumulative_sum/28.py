n, q = 5, 5
A = [[0] * (n+1) for _ in range((n+1))]

for i in range(q):
    a, b = map(int, input().split())
    # 加算するマス : 範囲の左上のマスと、範囲の右下の 1 つ右、かつ 1 つ下のマス
    A[2][a-1] += 1
    A[3][b] += 1
    # 減算するマス : 範囲の右上の右隣のマス、範囲の左下の直下のマス、つまり範囲から 1 マス出たマス
    A[2][b] -= 1
    A[3][a-1] -= 1

for i in range(n+1):
    for j in range(n):
        A[i][j+1] += A[i][j]
for i in range(n):
    for j in range(n+1):
        A[i+1][j] += A[i][j]

max_value = 0
for line in A:
    max_value = max(max_value, max(line))

print(max_value)

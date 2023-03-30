n, k = map(int,input().split())
A = [[0] * (n+1) for _ in range((n+1))]

for i in range(k):
    a, b, c, d = map(int, input().split())
    # top_left: (a,b), right_bottom: (c,d)
    # 加算するマス : 範囲の左上のマスと、範囲の右下の 1 つ右、かつ 1 つ下のマス
    A[b-1][a-1] += 1
    A[d][c] += 1
    # 減算するマス : 範囲の右上の右隣のマス、範囲の左下の直下のマス、つまり範囲から 1 マス出たマス
    A[b-1][c] -= 1
    A[d][a-1] -= 1

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

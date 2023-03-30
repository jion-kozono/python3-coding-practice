n, q = 5, 5
a = [[0] * (n+1) for _ in range((n+1))]
# x1 = x2 = y1 = y2 = [0] * (q+1)
x1 = [1,2,3,1,3]
x2 = [3,4,5,3,5]
y1 = [1,2,3,3,1]
y2 = [3,4,5,5,3]

# 例えば、左上が (1, 1), 右下が (3, 3) の長方形の範囲にそれぞれ 1 を加算したいとき、(1, 1), (4, 4) に 1 を加算し、(1, 4), (4, 1) から 1 を減算します。
for i in range(q):

    # 加算するマス : 範囲の左上のマスと、範囲の右下の 1 つ右、かつ 1 つ下のマス
    a[y1[i]-1][x1[i]-1] += 1
    a[y2[i]][x2[i]] += 1
    # 減算するマス : 範囲の右上の右隣のマス、範囲の左下の直下のマス、つまり範囲から 1 マス出たマス
    a[y1[i]-1][x2[i]] -= 1
    a[y2[i]][x1[i]-1] -= 1

for i in range(n):
    for j in range(n):
        a[i][j+1] += a[i][j]
for i in range(n):
    for j in range(n):
        a[i+1][j] += a[i][j]

max_value = 0
for line in a:
    max_value = max(max_value, max(line))

print(max_value)

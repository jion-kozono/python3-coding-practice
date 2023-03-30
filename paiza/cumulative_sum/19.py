# https://paiza.jp/works/mondai/reviews/show/0a9afd362bcb1c041d39dae86e6a33f0

a,b = map(int,input().split())
n = 5
A = [list(map(int, input().split())) for _ in range(n)]

s = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 領域を [sx, gx) × [sy, gy) とした長方形領域の整数の和は
# s_{gy, gx} - s_{sy, gx} - s_{gy, sx} + s_{sy, sx}
# 左上の座標を (a, 3), 右下の座標を (b, 3) としたとき、この領域は [a, b + 1) * [3, 4)と考えることができるので、これを二次元配列 s を用いて表すと
# s[b + 1][4] - s[a][4] - s[b + 1][3] + s[a][3]
for i in range(n):
    for j in range(n):
        # s_{y + 1, x + 1} = s_{y, x + 1} + s_{y + 1, x} - s_{y, x} + A_{y, x}
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

# クエリ [x1, x2) × [y1, y2) の長方形区域の和
# s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]
print(s[b+1][4] - s[a][4] - s[b+1][3] + s[a][3])

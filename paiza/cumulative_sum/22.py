# https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__2dsection_sum_step4

n,m,q= map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    a,b,c,d = map(int,input().split())

    s = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # 領域を [sx, gx) × [sy, gy) とした長方形領域の整数の和は
    # s_{gy, gx} - s_{sy, gx} - s_{gy, sx} + s_{sy, sx}
    # クエリ [x1, x2) × [y1, y2) の長方形区域の和
    # s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]
    # x: [a, c) * y: [b, d)
    # s[c+1][d+1] - s[a][d+1] - s[c+1][b] + s[a][b]

    for i in range(n):
        for j in range(m):
            # s_{y + 1, x + 1} = s_{y, x + 1} + s_{y + 1, x} - s_{y, x} + A_{y, x}
            s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

    print(s[c+1][d+1] - s[a][d+1] - s[c+1][b] + s[a][b])

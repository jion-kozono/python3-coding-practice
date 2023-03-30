# https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__2dsection_sum_step1

# 長方形領域の左上の要素を A_{1, 1}, 右下の要素を A_{3, 3} としたとき、この長方形領域内の整数の和を累積和を用いて求め、一行で出力してください。


n = 5
A = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = i+j+1

s = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        # s_{y + 1, x + 1} = s_{y, x + 1} + s_{y + 1, x} - s_{y, x} + A_{y, x}
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

# (長方形領域内の整数の和) = s_{gy, gx} - s_{sy, gx} - s_{gy, sx} + s_{sy, sx}
print(s[4][4] - s[4][1] - s[1][4] + s[1][1]) #1,1は重複分

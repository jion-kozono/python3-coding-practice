n = int(input())
points = [map(int, input().split()) for _ in range(n)]
xs,xt = map(int, input().split())
ys,yt = map(int, input().split())

# n 個の点のうち、(x_s, y_s), (x_s, y_t), (x_t, y_t), (x_t, y_s) の4頂点からなる長方形の内部に含まれている点の数を求めてください。なお、長方形の辺上にある点は長方形に含まれているものとします。
# ・ x_s < x_t
# ・ y_s < y_t
ans = 0
for xi, yi in points:
    if xs <= xi <= xt and ys <= yi <= yt:
        ans += 1

print(ans)

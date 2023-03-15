N, M, Q = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())

    # 頂点番号を0始まりにする
    u -= 1
    v -= 1

    # グラフに辺を追加
    G[u].append(v)
    G[v].append(u)

# 初期状態の各頂点の色を入力
col = list(map(int, input().split()))

# 各クエリに答える
for i in range(Q):
    t,x,*y = map(int, input().split())

    # 頂点番号を0始まりにする
    x -= 1

    # 頂点 x の色を出力
    print(col[x])

    # タイプ1の場合
    if t == 1:
        # 頂点 xに隣接する各頂点 v の色を更新
        for v in G[x]:
            col[v] = col[x]
    # タイプ2の場合
    else:
        # 頂点 x の色をyに更新
        col[x] = y[0]

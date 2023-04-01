from queue import Queue

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

H, W = map(int, input().split())
S = [input() for _ in range(H)]

que = Queue()
dist = [[-1] * W for _ in range(H)]

que.put((0,0))
dist[0][0] = 0

while not que.empty():
    x, y = que.get()

    for dx,dy in zip(DX,DY):
        x2, y2 = x+dx, y+dy

        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W:
            continue

        if S[x2][y2] == "#":
            continue

        if dist[x2][y2] != -1:
            continue

        que.put((x2,y2))
        dist[x2][y2] = dist[x][y] +1

white = sum(line.count('.') for line in S)

if dist[H-1][W-1] != -1:
    # 最短経路の白マスの個数は(距離-1)
    # 全ての白マスから最短経路の白マスを引いた個数が黒に濡れる
    print(white - dist[H-1][W-1] -1)
else:
    print(-1)

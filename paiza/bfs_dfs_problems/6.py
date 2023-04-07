from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = deque()
q.append((sy, sx))
S[sy][sx] = "*"
# visited = [[False] * W for _ in range(H)]
# visited[sy][sx] = True
dist = [[-1] * W for _ in range(H)]
dist[sy][sx] = 0

while q:
    ny, nx = q.popleft()
    if ny == gy and nx == gx:
        print(dist[ny][nx])
        exit()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= ny + dy < H and 0 <= nx + dx < W:
            if dist[ny + dy][nx + dx] == -1 and S[ny + dy][nx + dx] != "#":
                dist[ny + dy][nx + dx] = dist[ny][nx] + 1
                q.append((ny + dy, nx + dx))

print("No")

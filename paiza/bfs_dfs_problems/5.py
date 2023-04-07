from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = deque()
q.append((sy, sx))
S[sy][sx] = "*"
visited = [[False] * W for _ in range(H)]
visited[sy][sx] = True

while q:
    ny, nx = q.popleft()
    if ny == gy and nx == gx:
        print("Yes")
        exit()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= ny + dy < H and 0 <= nx + dx < W:
            if not visited[ny + dy][nx + dx] and S[ny + dy][nx + dx] != "#":
                visited[ny + dy][nx + dx] = True
                q.append((ny + dy, nx + dx))

print("No")

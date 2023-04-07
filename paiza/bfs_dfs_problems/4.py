from collections import deque

H, W, N = map(int, input().split())
y, x = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = deque()
q.append((y, x))
l = [[-1] * W for _ in range(H)]
l[y][x] = 0
S[y][x] = "*"

while q:
    ny, nx = q.popleft()
    if l[ny][nx] == N:
        continue
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= ny + dy < H and 0 <= nx + dx < W:
            if l[ny + dy][nx + dx] == -1 and S[ny + dy][nx + dx] != "#":
                l[ny + dy][nx + dx] = l[ny][nx] + 1
                S[ny + dy][nx + dx] = "*"
                q.append((ny + dy, nx + dx))

for i in range(H):
    print(*S[i], sep="")

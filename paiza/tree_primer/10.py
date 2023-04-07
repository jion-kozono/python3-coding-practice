from collections import deque

N, R = map(int, input().split())

g = [[] for _ in range(N)]
edge = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N - 1):
    a, b = edge[i]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(R - 1)
dist = [N] * N
dist[R - 1] = 0
while q:
    now = q.popleft()
    for nxt in g[now]:
        if dist[nxt] == N:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

for i in range(N - 1):
    a, b = edge[i]
    a -= 1
    b -= 1
    if dist[a] < dist[b]:
        print("A")
    else:
        print("B")

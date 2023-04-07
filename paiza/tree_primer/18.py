from collections import deque

N, A, X = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(A - 1)
dist = [1000] * N
dist[A - 1] = 0
while q:
    now = q.popleft()
    for nxt in g[now]:
        if dist[nxt] == 1000:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

for i in range(N):
    if dist[i] == X:
        print(i + 1)

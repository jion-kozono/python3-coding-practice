#https://paiza.jp/works/mondai/tree_primer/tree_primer__path
from collections import deque

def bfs(s: int) -> list:
    dist = [-1] * N
    dist[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        for nxt in g[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    return dist

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

dist_from_zero = bfs(0)
max_dist = max(dist_from_zero)
for i, j in enumerate(dist_from_zero):
    if j == max_dist:
        diameter = max(bfs(i))
        print(diameter)
        break

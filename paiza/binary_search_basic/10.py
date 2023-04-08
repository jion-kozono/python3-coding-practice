#https://paiza.jp/works/mondai/tree_primer/tree_primer__path
from collections import deque

N, A, B = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(A-1)
prev = [-1] * N
visited = [False] * N
visited[A - 1] = True

while q:
    now = q.popleft()
    if now == B-1:
        break
    for next in g[now]:
        if not visited[next]:
            visited[next] = True
            prev[next] = now
            q.append(next)

temp = B-1
ans = []
while temp != -1:
    ans.append(temp)
    temp = prev[temp]

for i in ans[::-1]:
    print(i+1)

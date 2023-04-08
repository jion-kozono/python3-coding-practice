import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
from collections import deque

def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, X, Y = MI()
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = MI()
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(X-1)
dist = [-1] * N
dist[X - 1] = 0
prev = [-1] * N

while q:
    now = q.popleft()
    if now == Y - 1:
        break
    for next in g[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            prev[next] = now
            q.append(next)

tmp = Y - 1
ans = []
while tmp != -1:
    ans.append(tmp)
    tmp = prev[tmp]

for i in ans[::-1]:
    print(i + 1)

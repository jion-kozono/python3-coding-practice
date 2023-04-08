import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
from collections import deque

def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, M, X,Y = MI()
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = MI()
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
for i in range(N):
    g[i].sort()

q = deque()
q.append(X - 1)
dist = [-1] * N
dist[X - 1] = 0
while q:
    now = q.popleft()
    for nxt in g[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

print(dist[Y-1])

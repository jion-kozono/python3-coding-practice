import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
from collections import deque

def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, M,X = MI()
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
unvisited = [True] * N
unvisited[X - 1] = False
while q:
    now = q.popleft()
    print(now + 1)
    for nxt in g[now]:
        if unvisited[nxt]:
            unvisited[nxt] = False
            q.append(nxt)

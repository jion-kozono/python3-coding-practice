import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, X = MI()
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = MI()
    g[a].append(b)
    g[b].append(a)

g[X].sort()
for ans in g[X]:
    print(ans)

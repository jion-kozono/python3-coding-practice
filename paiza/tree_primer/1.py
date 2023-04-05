import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
G = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    a, b = MI()
    a-=1
    b-=1
    G[a][b] = G[b][a] = 1

for i in range(n):
    print(*G[i])

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
G = [[] for _ in range(n)]

for i in range(n-1):
    a, b = MI()
    G[a-1].append(b)
    G[b-1].append(a)

for i in range(n):
    if len(G[i]) == 1:
        print(i+1)

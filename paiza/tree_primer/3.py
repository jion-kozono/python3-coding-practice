import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
G = [[] for _ in range(n)]

for i in range(n-1):
    a, b = MI()
    G[a-1].append(b)
    G[b-1].append(a)

for i in range(k):
    a, b = MI()
    if b in G[a-1] or a in G[b-1]:
        print("YES")
    else:
        print("NO")

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, Q = MI()
LRs = [LI() for _ in range(Q)]

s = [0] * (N+1)

for i in range(Q):
    l, r = LRs[i]
    l-=1
    r-=1
    s[l] += 1
    s[r+1] -= 1

for i in range(N):
    s[i+1] += s[i]

print(max(s))

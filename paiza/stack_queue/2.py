import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = []
Q = I()
for _ in range(Q):
    query = LI()
    if query[0] == 2:
        continue
    x = query[1]
    N.append(x)

print(len(N))
for n in N:
    print(n)

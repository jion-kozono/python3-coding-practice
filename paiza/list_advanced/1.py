import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N,M = MI()

A = LS()
B = LS()
X = LI()

line = []

for a in A:
    line.append(a)

for i in range(M):
    line.insert(X[i]-1, B[i])

for p in line:
    print(p)

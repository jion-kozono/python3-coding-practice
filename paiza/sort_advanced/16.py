import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,q = MI()
A = LI()

for i in range(q):
    query, k, x = MS()
    k = int(k)-1
    x = int(x)
    if query == "update":
        A[k] = x
    else:
        print(sorted(A, reverse=True)[k])

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,q= MI()
A = LI()
K = LI()

A.sort(reverse=True)
for i in range(q):
    print(A[K[i]-1])

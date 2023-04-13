import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,l,r= MI()
l-=1
r-=1
A = LI()

range_A = sorted(A[l:r])
A = A[:l] + range_A + A[r:]
print(*A)

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
A = LI()

A.sort()
can = True
level = 1
for i in range(n):
    if A[i] > level:
        can=False
        break
    else:
        level = A[i] +1

print("Yes" if can else "No")

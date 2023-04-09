import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,m = MI()
A = LI()
B = LI()

for i in range(n - m + 1):
    if A[i : i + m] == B:
        print(i + 1)
        break
else:
    print(-1)

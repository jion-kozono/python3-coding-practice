import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,m,k,x = MI()

for i in range(n):
    s = S()
    col = s.split(",")
    target = int(col[k-1])
    if target >= x:
        print(s)

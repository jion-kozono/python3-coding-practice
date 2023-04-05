import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())


# H(x) = (a * x + b) % mod
n, a, b, mod = MI()
for i in range(n):
    x = I()
    print((a * x + b) % mod)

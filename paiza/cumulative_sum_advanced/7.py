import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

Q = I()
LRs = [LI() for _ in range(Q)]

s = [0] * (1011)

for x in range(1, 1010):
    if x % 3 == 0 and x % 5 == 0:
        s[x+1] = s[x] + 1
    else:
        s[x+1] = s[x]

for i in range(Q):
    l, r = LRs[i]
    print(s[r+1] - s[l])

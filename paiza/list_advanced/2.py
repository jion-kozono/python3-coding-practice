import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N,Q = MI()

cups = [0 for _ in range(N)]
cups[0] = 1

for _ in range(Q):
    op, x, y = MI()
    x-=1
    y-=1
    if op == 1: # swap
        if y >= len(cups):
            y = len(cups) -1
        cups[x], cups[y] = cups[y], cups[x]
    else: # insert
        cups.insert(y, 0)

for i in range(len(cups)):
    if cups[i] == 1:
        print(i+1)

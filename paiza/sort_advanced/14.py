import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
y_xs = [[0, 0] for _ in range(n)]
for i in range(n):
    y,x = MI()
    y_xs[i][0] = y
    y_xs[i][1] = x

y_xs.sort(key=lambda y_x: abs(y_x[0])+abs(y_x[1]))

for i in range(n):
    print(*y_xs[i])

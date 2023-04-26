import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
points = [LF() for _ in range(N)]
Ps = LI()

# √((x_1-x_2)^2 + (y_1-y_2)^2)
def calc_dist(a,b):
    return math.sqrt(pow(a[0] - b[0], 2.0) + pow(a[1] - b[1], 2.0))

dist = 0

for i in range(N):
    dist += calc_dist(points[Ps[i-1]-1], points[Ps[(i) % N]-1]) # 総数での余りを計算することで、始点に戻れる

print(dist)

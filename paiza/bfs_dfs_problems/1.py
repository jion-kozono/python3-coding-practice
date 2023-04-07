import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

H, W = MI()
y, x = MI()

g = [[0 for _ in range(W)] for _ in range(H) ]

# (y+1,x), (y-1,x), (y,x+1), (y,x-1)
g[y][x] = 1
if y+1 < H:
  g[y+1][x] = 1
if y-1 >= 0:
  g[y-1][x] = 1
if x+1 < W:
  g[y][x+1] = 1
if x-1 >= 0:
  g[y][x-1] = 1

for i in range(H):
    for j in range(W):
        if g[i][j] == 1:
            print("*", end="")
        else:
            print(".", end="")
    print()

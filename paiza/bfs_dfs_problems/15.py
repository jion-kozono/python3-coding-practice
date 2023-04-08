import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
from collections import deque

def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

def dfs(y: int, x: int):
    S[y][x] = '#'
    for i in range(-1, 2, 2):
        if 0 <= y + i < H and S[y + i][x] == '.':
            dfs(y + i, x)
        if 0 <= x + i < W and S[y][x + i] == '.':
            dfs(y, x + i)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            dfs(i, j)
            ans += 1

print(ans)

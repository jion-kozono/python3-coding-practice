import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
from collections import deque

def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

H, W, y, x = MI()

def dfs(times, y, x):
    if times == 3:
        print(y, x)
    else:
        if 0 <= y - 1:
            dfs(times + 1, y - 1, x)
        if x + 1 < W:
            dfs(times + 1, y, x + 1)
        if y + 1 < H:
            dfs(times + 1, y + 1, x)
        if 0 <= x - 1:
            dfs(times + 1, y, x - 1)
dfs(0, y, x)

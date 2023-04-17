import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, W, H = MI()
A = [LI() for _ in range(N)]

s = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + A[i][j]

max_value = 0
for i in range(N-H+1):
    for j in range(N-W+1):
        max_value = max(max_value, s[i+H][j+W] - s[i][j+W] - s[i+H][j] + s[i][j])
print(max_value)

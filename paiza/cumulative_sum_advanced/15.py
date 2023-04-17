import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, Q, M = MI()
A = [LI() for _ in range(N)]
XYs = [LI() for _ in range(Q)]

s = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(Q):
    x, y = XYs[i]
    x-=1
    y-=1
    s[y][x] += 1
    s[y+M][x] -= 1
    s[y][x+M] -= 1
    s[y+M][x+M] -= 1

# 縦方向と横方向でそれぞれ累積和をとる
# 横
for i in range(N + 1):
    for j in range(N + 1):
        if j > 0:
            s[i][j] += s[i][j - 1]
# 縦
for i in range(N + 1):
    for j in range(N + 1):
        if i > 0:
            s[i][j] += s[i - 1][j]

kill_count = 0
for i in range(N):
    for j in range(N):
        if s[i][j] >= A[i][j]:
            kill_count += 1

print(kill_count)

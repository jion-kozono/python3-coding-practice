import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, P = MI()
A = [LI() for _ in range(N)]

s = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + A[i][j]

# https://paiza.jp/works/mondai/reviews/show/c1a15faedc166a2ce415f1585ef9152b

max_value = 0
for sx in range(N):
    for sy in range(N):
        for ex in range(sx, N):
            for ey in range(sy, N):
                value = s[ex + 1][ey + 1] - s[sx][ey + 1] - s[ex + 1][sy] + s[sx][sy]
                area = (ex - sx + 1) * (ey - sy + 1)
                if area <= P:
                    max_value = max(max_value, value)
print(max_value)

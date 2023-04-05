import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
num_of_vertex = N

exist = [1] * N
g = [[0] * N for _ in range(N)]

for i in range(N - 1):
    a, b = MI()
    a -= 1
    b -= 1
    g[a][b] = 1
    g[b][a] = 1

while num_of_vertex > 2:
    for i in range(N):
        cnt = 0
        for j in range(N):
            if g[i][j] == 1:
                cnt += 1
        if cnt == 1:
            num_of_vertex -= 1
            exist[i] = 0
            g[i] = [0] * N

    for i in range(N):
        for j in range(N):
            if exist[j] == 0 and g[i][j] == 1:
                g[i][j] = 0

for i in range(N):
    if exist[i] == 1:
        print(i + 1)

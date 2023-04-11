import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, m, h, x = MI()
max_sum = 0
A = [[LI() for _ in range(n)] for _ in range(h)]

count = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if A[k][i][j] == x:
                count +=1
print(count)

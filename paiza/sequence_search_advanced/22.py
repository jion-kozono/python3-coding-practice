import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, m, k = MI()
max_sum = 0
A = [LI() for _ in range(n)]
for i in range(n-k+1):
    for j in range(m-k+1):
        temp = 0
        for s in range(k):
            for t in range(k):
                temp += A[i+s][j+t]
        max_sum = max(max_sum, temp)
print(max_sum)

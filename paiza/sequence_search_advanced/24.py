import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, m, k, x = MI()
count = 0
A = [LI() for _ in range(n)]

count = 0
for i in range(n-k+1):
    for j in range(m-k+1):
        can = True
        for s in range(k):
            for t in range(k):
                if A[i+s][j+t] > x:
                    can = False
                    break
            if not can:
                break
        if can:
            count +=1
print(count)

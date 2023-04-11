import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, m, k = MI()
count = 0
for i in range(n):
    A = LI()
    for j in range(m):
        if A[j] == k:
            count+=1
print(count)

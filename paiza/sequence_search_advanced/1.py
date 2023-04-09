import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
A = LI()

ans = 0
# a_i = a_{ i + 1 }
for i in range(n-1):
    if A[i] == A[i+1]:
        ans += 1
print(ans)

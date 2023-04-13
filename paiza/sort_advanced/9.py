import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, x = MI()
A = LI()
A.sort(reverse=True)

ans = 0
temp = 0
for i in range(n):
    temp +=A[i]
    ans +=1
    if temp >= x:
        break
else:
    ans = -1
print(ans)

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, K = MI()
K-=1
a = LI()
s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + a[i]

max_num = 0
for i in range(N - K -1):
    max_num = max(max_num, s[i+K+1] - s[i])
print(max_num)

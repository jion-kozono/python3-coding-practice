import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
A = LI()
s = [0] * (N+1)

for i in range(N):
    s[i+1] = s[i] + A[i]

ans = 10001
for i in range(N-1):
    sum1 = s[i + 1]
    sum2 = s[N] - s[i + 1]
    ans = min(ans, abs(sum1 - sum2))

print(ans)

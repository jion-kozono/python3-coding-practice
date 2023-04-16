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
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(N):
    left[i + 1] = max(left[i], A[i])
    right[i + 1] = max(right[i], A[N - i - 1])

for k in range(1, N-1):
    print(min(left[k], right[N-k-1]))

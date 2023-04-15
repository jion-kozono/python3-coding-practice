import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, X, Y, C = MS()
N, X, Y = map(int, (N, X, Y))
s = S()
sum_s = [0] * (N+1)

for i in range(N):
    if s[i] == C:
        sum_s[i+1] = sum_s[i] + 1
    else:
        sum_s[i+1] = sum_s[i]

print(sum_s[Y]-sum_s[X-1])

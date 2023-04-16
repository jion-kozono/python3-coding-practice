import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, A, B = MI()
st = S()
b = [0] * (N)
sum_piz = [0] * (N+1)
for i in range(N-2):
    if st[i:i+3] == "piz":
        b[i] = 1

for i in range(N):
    sum_piz[i+1] = sum_piz[i] + b[i]

print(sum_piz[B-2] - sum_piz[A-1])

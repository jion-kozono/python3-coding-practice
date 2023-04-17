import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

Q, M = MI()
STPs = [LI() for _ in range(Q)]

time = [0] * 1010

for i in range(Q):
    s, t, p = STPs[i]
    time[s] += p
    time[t+1] -= p

for i in range(1001):
    time[i+1] += time[i]

can = "Yes"
for i in range(1001):
    if time[i] >= M:
        can = "No"
        break

print(can)

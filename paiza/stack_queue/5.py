import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = collections.deque()
Q = I()
for _ in range(Q):
    query = LS()
    if query[0] == "1":
        x = query[1]
        N.append(x)
    else:
        N.popleft()
    print(*N)

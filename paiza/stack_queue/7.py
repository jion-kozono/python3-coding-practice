import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = collections.deque()
N2 = collections.deque()
Q = I()
for _ in range(Q):
    query = LI()
    if query[0] == 1:
        k, x = query[1:]
        if k == 1:
            N.append(x)
        else:
            N2.append(x)
    elif query[0] == 2:
        k = query[1]
        if k == 1:
            print(N[0])
            N.popleft()
        else:
            print(N2[0])
            N2.popleft()
    else:
        print(len(N), len(N2))

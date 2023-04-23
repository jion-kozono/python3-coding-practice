import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
X = [I() for _ in range(n)][::-1]
k = I()

s = collections.deque(X)

for i in range(k):
    q = LS()
    query = q[0]
    if query == "return":
        x = int(q[1])
        s.appendleft(x)
    else:
        s.popleft()

while s:
    print(s.popleft())

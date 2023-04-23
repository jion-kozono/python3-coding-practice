import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
items = collections.deque()

for i in range(n):
    q = LS()
    query = q[0]
    if query == "add":
        num = int(q[1])
        items.append(num)
    else:
        x = int(q[1])
        while x:
            items.popleft()
            x-=1

while items:
    print(items.popleft())

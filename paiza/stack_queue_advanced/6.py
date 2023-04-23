import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()

queue1 = collections.deque()
queue2 = collections.deque()
queue3 = collections.deque()

for i in range(n):
    q = LS()
    query = q[0]
    s = int(q[1])
    if query == "push":
        x = int(q[2])
        if s == 1:
            queue1.append(x)
        elif s == 2:
            queue2.append(x)
        else:
            queue3.append(x)
    else:
        if s == 1:
            queue1.popleft()
        elif s == 2:
            queue2.popleft()
        else:
            queue3.popleft()

while queue1:
    print(queue1.popleft())
while queue2:
    print(queue2.popleft())
while queue3:
    print(queue3.popleft())

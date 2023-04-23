import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()

stack1 = collections.deque()
stack2 = collections.deque()
stack3 = collections.deque()

for i in range(n):
    q = LS()
    query = q[0]
    s = int(q[1])
    if query == "push":
        x = int(q[2])
        if s == 1:
            stack1.appendleft(x)
        elif s == 2:
            stack2.appendleft(x)
        else:
            stack3.appendleft(x)
    else:
        if s == 1:
            stack1.popleft()
        elif s == 2:
            stack2.popleft()
        else:
            stack3.popleft()

while stack1:
    print(stack1.popleft())
while stack2:
    print(stack2.popleft())
while stack3:
    print(stack3.popleft())

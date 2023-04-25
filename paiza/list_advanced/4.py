import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

Q = I()
dumbbell = collections.deque()

for i in range(Q):
    q = LS()
    if q[0] == "ADD_RIGHT":
        w = int(q[1])
        dumbbell.append(w)
    elif q[0] == "ADD_LEFT":
        w = int(q[1])
        dumbbell.appendleft(w)
    elif q[0] == "REMOVE_RIGHT":
        dumbbell.pop()
    else:
        dumbbell.popleft()

sum_w = 0
while dumbbell:
    sum_w += dumbbell.pop()

print(sum_w)

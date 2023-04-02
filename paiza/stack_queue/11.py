import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, K = MI()
A = LI()
time_count = A[-1]
time=0

queue = [0 for _ in range(K)]

for i in range(1, time_count+1):
    queue.pop(0)
    if i in A:
        queue.append(1)
        print(queue.count(1))
    else:
        queue.append(0)

# Queueを使ったやつ

N, K = MI()
A = LI()
time_count = A[-1]
person_on_escalator=0

queue = queue.Queue()
for i in range(K):
    queue.put(0)
for i in range(1, time_count+1):
    person_on_escalator -= queue.get()
    if i in A:
        queue.put(1)
        person_on_escalator+=1
        print(person_on_escalator)
    else:
        queue.put(0)

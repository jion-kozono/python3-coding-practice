import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, x = MI()
ridings = collections.deque()
ridings_sum = 0

for i in range(n):
    q = LS()
    query = q[0]
    if query == "ride":
        n = int(q[1])
        weights = list(map(int, q[2:]))
        for w in weights:
            if ridings_sum + w <= x:
                ridings.append(w)
                ridings_sum += w
    else:
        k = int(q[1])
        while k:
            ridings_sum -= ridings.pop()
            k-=1

print(len(ridings))
print(ridings_sum)

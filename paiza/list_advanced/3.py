import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N,Q = MI()
A = LI()
B = LI()

for i in range(Q):
    A = list(filter(lambda x: x % B[i] != 0, A))

if len(A):
    print("Kyoko")
else:
    print("You")

print(*A)

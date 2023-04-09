import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,m = MI()
A = LI()
B = LI()

match_count = 0
for i in range(n):
    if A[i] == B[match_count]:
        match_count += 1
    if match_count == m:
        print("Yes")
        break
else:
    print("No")

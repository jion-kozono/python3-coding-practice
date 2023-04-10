import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
A = LI()

count = 0
# a_i < a_{ i + 1 } > a_{ i + 2 } or
# a_i > a_{ i + 1 } < a_{ i + 2 }
for i in range(n-2):
    if (A[i] < A[i+1] and A[i+1] > A[i+2]) or (A[i] > A[i+1] and A[i+1] < A[i+2]):
        count+=1
print(count)

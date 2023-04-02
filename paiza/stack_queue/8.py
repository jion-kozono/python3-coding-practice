import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, X = MI()
A = LI()

max_sum =0
left_n = A[0]

for i in range(X):
    max_sum+=A[i]

tmp_sum = max_sum

for i in range(N-X):
    tmp_sum -= A[i]
    tmp_sum += A[i+X]
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        left_n = A[i+1]

print(max_sum, left_n)

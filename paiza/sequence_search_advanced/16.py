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

max_len = 1
temp_len = 1
prev_num = A[0]
for i in range(1,n):
    if prev_num == A[i]:
        temp_len+=1
    else:
        temp_len = 1
    max_len = max(temp_len, max_len)
    prev_num = A[i]
print(max_len)

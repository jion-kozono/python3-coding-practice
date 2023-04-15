import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, A, B = MI()
a_list = LI()
cumulative_sum = [0] * (N+1)
for i in range(N):
    a = a_list[i]
    cumulative_sum[i+1] = cumulative_sum[i] + a

print(cumulative_sum[B+1] - cumulative_sum[A])

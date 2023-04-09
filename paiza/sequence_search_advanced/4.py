import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,k = MI()
A = LI()

max_ans = -100 * k
ans_i = 1

for i in range(n-k+1):
    sum_of_three = sum(A[i:i+k])
    if max_ans <= sum_of_three:
        max_ans = sum_of_three
        ans_i = i
print(ans_i+1)

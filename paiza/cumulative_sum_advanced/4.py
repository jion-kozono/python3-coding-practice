import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
a = LI()
s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + a[i]

board_num = 0
max_num = 0
for i in range(1, N+1):
    board_num += s[i]
    max_num = max(max_num, board_num)
print(max_num)

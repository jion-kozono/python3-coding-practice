import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())


# H(x) = x.count('p') + x.count('a') + x.count('i') + x.count('z')
n = I()
for i in range(n):
    x = S()
    print(x.count('p') + x.count('a') + x.count('i') + x.count('z'))

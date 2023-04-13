import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
strings = [S() for _ in range(n)]
strings.sort(key=lambda x: (len(x), x))

for i in range(n):
    print(strings[i])

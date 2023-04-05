import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())


n = I()
for i in range(n):
    s = S()

    hash = 0
    for j in range(len(s)):
        hash += (j+1) * (ord(s[j])-ord('a')+1)

    hash %= 100

    print(hash)

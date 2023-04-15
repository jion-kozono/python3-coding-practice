import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

def extGCD(a, b):
    if b:
        d, y, x = extGCD(b, a%b)
        y -= (a//b) * x
        return d, x, y
    return a, 1, 0

A, B = MI()

_, x, y = extGCD(A,B)
print(x,y)

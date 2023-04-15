import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())
# https://paiza.jp/works/mondai/reviews/show/0ebbb5b6aaca137eaaafd1a9a169a1c0

def gcd(a,b):
    return gcd(b, a%b) if (a%b) else b

# A 分を測る砂時計と B 分を測る砂時計が与えられたとき、この 2 つの砂時計を用いて T 分を測ることができるかを判定してください。
A, B, T = MI()
# Ax + By = T
if T % gcd(A, B) == 0:
    print("Yes")
else:
    print("No")

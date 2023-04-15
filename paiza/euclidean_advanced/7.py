import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

A,B = MI()

def gcd(a, b):
    return gcd(b, a%b) if a%b else b
def lcm(a, b):
    return a*b//gcd(a,b)

print(lcm(A,B))

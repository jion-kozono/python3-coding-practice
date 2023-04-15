import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
A = [I() for _ in range(N)]

def gcd(a, b):
    return gcd(b, a%b) if a%b else b

def lcm(a, b):
    return a*b//gcd(a,b)

ans_gcd = A[0]
ans_lcm = A[0]
for i in range(1, N):
    ans_gcd = gcd(ans_gcd, A[i])
    ans_lcm = lcm(ans_lcm, A[i])

print(ans_gcd)
print(ans_lcm)

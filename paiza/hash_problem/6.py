import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

hash_table = [[] for _ in range(10)]

def hash(x): return x % 10

n = I()
for i in range(n):
    x = I()

    h = hash(x)
    hash_table[h].append(x)

for i in range(10):
    print(*hash_table[i])

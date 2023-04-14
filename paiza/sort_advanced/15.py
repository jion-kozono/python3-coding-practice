import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,q = MI()
A = LI()
X = LI()

compressed = {a_i: i + 1 for i, a_i in enumerate(sorted(A))}

for x_i in X:
    print(compressed[x_i])

# # 以下はタイムアウト
# A.sort()
# for i in range(q):
#     print(A.index(X[i])+1)

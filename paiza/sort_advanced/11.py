import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, m, k = MI()
k-=1
A = [[0 for _ in range(m)] for _ in range(n)]

# 先頭にkを挿入
for i in range(n):
    a = LI()
    for j in range(m):
        if j == k:
            A[i][0] = a[j]
        elif j < k:
            A[i][j+1] = a[j]
        else:
            A[i][j] = a[j]

A.sort()
# kを元の位置に戻す
sorted_A = [[] for _ in range(n)]
for i in range(n):
    for j in range(1, k+1): # kの前まで挿入
        sorted_A[i].append(A[i][j])
    sorted_A[i].append(A[i][0]) # kを挿入
    for j in range(k+1, m):
        sorted_A[i].append(A[i][j])



for i in range(n):
    print(*sorted_A[i])

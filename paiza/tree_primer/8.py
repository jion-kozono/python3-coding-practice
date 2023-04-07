import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())
# https://paiza.jp/works/mondai/reviews/show/af095c8beaaff9ec0500b076a8121bd6

N, K, R = MI()

class Node:
    def __init__(self):
        self.parents = []

tree = [Node() for _ in range(N)]

for _ in range(N - 1):
    a, b = MI()
    b-=1
    tree[b].parents.append(a)

for i in range(N):
    tree[i].parents.sort()

for i in range(K):
    v = I()
    v-=1

    print(*tree[v].parents)

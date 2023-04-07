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
        self.parent = -1
        self.children = []

tree = [Node() for _ in range(N)]

for _ in range(N - 1):
    a, b = MI()
    a-=1
    tree[a].children.append(b)

for i in range(N):
    tree[i].children.sort()

for i in range(K):
    v = I()
    v-=1

    print(*tree[v].children)

# 隣接リスト
# g = [[] for _ in range(N)]
# for _ in range(N - 1):
#     a, b = MI()
#     g[a - 1].append(b)

# for i in range(N):
#     g[i].sort()

# for _ in range(K):
#     v = int(input())
#     print(*g[v - 1])

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())
# https://paiza.jp/works/mondai/reviews/show/af095c8beaaff9ec0500b076a8121bd6

N, R = MI()

class Node:
    def __init__(self):
        self.parents = []

tree = [Node() for _ in range(N)]

is_heap = True
for _ in range(N - 1):
    a, b = MI()
    if a < b:
        is_heap = False
        break
print("YES" if is_heap else "NO")

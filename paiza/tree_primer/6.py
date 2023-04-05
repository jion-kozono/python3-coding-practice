import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

# https://paiza.jp/works/mondai/reviews/show/cf7024a8493abf577ee107c8f18cd22c

# b を中心とする三角形の個数は 「b に接続する頂点からなる、相異なる 2 つの頂点のペアの数」と一致します。
# この数は、b に接続する辺の数を E(b) をすると E(b) C 2 = E(b) × (E(b)-1) / 2となります。

N = I()

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

num_of_triangles = 0
for i in range(N):
    num_of_triangles += len(g[i]) * (len(g[i]) - 1) // 2

if num_of_triangles % 2 == 0:
    print("erik")
else:
    print("paiza")

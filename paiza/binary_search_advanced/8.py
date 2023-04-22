import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
ABC = [LI() for _ in range(n)]
a, b, c = [list(i) for i in zip(*ABC)]

c.sort()

# 自分が勝った時は true, paiza 君が勝った時は false を返す
def check(x):
    # ab : x の時の自分の整数
    ab = []
    for i in range(n):
        ab.append(a[i] * x + b[i])
    ab.sort()

    pos = 0
    for i in range(n):
        if ab[i] > c[pos]:
            pos += 1
    # 自分の半分以上のカードがpaiza君が持っているcの配列のカードより大きい => 自分の勝利
    if pos > n / 2:
        return 1
    else:
        return 0

ng, ok = -(1<<24), 1<<24
while abs(ok - ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

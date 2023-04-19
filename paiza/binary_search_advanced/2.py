import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
abc = [LI() for _ in range(n)]

# 木の高さの最小値が K 以上になるタイミングを求めればよいです。
# 木の高さは常に増え続けるので、高さの最小値も常に増え続けます。
# このような単調性をもつ値の境界は、二分探索を用いて高速に求めることができます。
# 秒数を固定して計算したとき、高さが K 未満の木があればそれより後になり、すべての木の高さが K 以上ならその秒数以前になります。
# したがって、高さが K 未満の木が存在するような最大秒数を left, すべての木の高さが K 以上であるような最小秒数を right として、中央の値 mid を用いて判定、更新を繰り返せばよいです。
# 別解として、それぞれの木について高さ K 以上になる秒数を二分探索によって求め、それらの秒数の最大値を計算することでも求めることができます。

def check(t):
    for a, b, c in abc:
        if a * t * t + b * t + c < k:
            return 0
    return 1

ng, ok = 1, 1<<24
while (abs(ok - ng)) > 1:
    mid = (ok+ng) //2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)

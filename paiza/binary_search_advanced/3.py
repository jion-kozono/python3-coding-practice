import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
abcd = [LI() for _ in range(n)]

# すべての商品を 1 つずつそろえればよいので、x 日目にかかる最小費用は、すべての i について min(Aix + Bi, Cix + Di) を足し合わせた値になります。
# 商品の価格は常に増え続けるので、x 日目にかかる最小費用も増え続けます。
# したがって、最小費用が K 以下である最大日数を二分探索で求めればよいです。
# 日数を固定して計算したとき、最小費用が K 以下であればそれ以後になり、K より大きければその日数より前になります。
# したがって、最小費用が K 以下であるような最大日数を left, K より大きいような最小日数を right として、中央の値 mid を用いて判定、更新を繰り返せばよいです。

def check(x):
    sum = 0
    for a,b,c,d in abcd:
        sum += min(a * x + b, c * x + d)
    if(sum <= k) : return 1
    else : return 0

ok, ng = 0, int(1e+6)
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if(check(mid)): ok = mid
    else : ng = mid
print(ok)

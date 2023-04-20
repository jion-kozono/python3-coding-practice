import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
A = [I() for _ in range(n)]

# 全員が高さ x 以上になるために必要な燃料の個数を考えてみましょう。
# それぞれ i 番目の人は燃料 1 つにつき Ai だけ上昇することができるので、高さ x 以上になるために必要な燃料の個数は、x / Ai を切り上げた値になります。
# この値の合計、すなわち必要な燃料の個数が K 以下であるような最大の x を求めればよいです。
# 高さ x が増えれば、必要な燃料の個数が増えます。この単調性から、二分探索を用いて探索できることが分かります。
# したがって、必要な燃料の個数が K 以下であるような最大の高さを left, K より大きいような最小の高さを right として、中央の値 mid を用いて判定、更新を繰り返せばよいです。
# ちなみに、x / y を切り上げた値を求める際には、(x + y - 1) / y を切り捨てた値を用いることができます。

# 最小値で二分探索をする
# k個以内でジャンプできるときは true, できないときは false
def is_ok(x):
    # cnt : 燃料の個数
    cnt = 0
    for i in range(n):
        # x / y を切り上げた値を求める際には、(x + y - 1) / y を切り捨てた値を用いる
        cnt += (x + A[i] - 1) // A[i] # 高さ x 以上になるために必要な燃料の個数は、x / Ai を切り上げた値

    return 1 if cnt <= k else 0

ok, ng = 0, 1<<47
while abs(ok-ng) > 1:
    mid = (ng+ok) // 2
    if(is_ok(mid)): ok = mid
    else : ng = mid
print(ok)

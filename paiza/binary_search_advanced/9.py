import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

# https://paiza.jp/works/mondai/reviews/show/ad8310825513891480d95f1a215ced7e
# x を固定したときに、数列 A の連続部分列のうち最小値が x 以下のものが何個あるか考えましょう。
# 最小値が x 以下であるということは、その連続部分列に x 以下の要素を含むということになります。
# 逆に、すべて x より大きい要素から構成されている連続部分列の最小値は、x よりも大きいということになります。
# このことから、最小値が x より大きい連続部分列は、数列 A のうち x より大きい要素が連続している部分から取りだしたものであることがわかります。
# 長さ m の数列に含まれる連続部分列の個数が m × (m + 1) / 2 であることを用いて、x より大きい要素が連続している各部分について、その連続部分列の個数を足し合わせることで、最小値が x より大きい連続部分列の総数を求めることができます。
# あとは、これをすべての連続部分列の個数 n × (n + 1) / 2 から引くことで、最小値が x 以下である連続部分列の個数を求めることができます。
# よって、そのようにして求めた連続部分列の個数が K 以上であるような最小の x を求めればよいです。
# x が大きくなるほど、求める連続部分列の個数は多くなります。
# この単調性から、二分探索を用いて探索できることが分かります。
# したがって、求める連続部分列の個数が K より小さいような最大の x を left, K 以上であるような最小の x を right として、中央の値 mid を用いて判定、更新を繰り返せばよいです。
# 判定部分では、配列 A の要素を順番に見ていき、その要素が mid より大きければカウントを増やし、そうでなければ連続部分列の個数を引いてカウントをリセットします。
# 配列の末尾に番兵として非常に小さい値を追加しておくと、判定部分での最後の処理を省略することができます。

n, k = MI()
a = LI()
a.append(0) # 番兵

# 数列の k 番目の要素よりも小さくなる時 true, 大きくなる時 false
def check(x):
    # x より大きい要素を持つときの連続部分列の個数を求める
    # sum : 数列の K 番目の要素 = (全ての連続部分列の個数) - (x より大きい要素を持つときの連続部分列の個数)
    sum = n * (n+1) / 2
    cnt = 0
    for i in range(n+1):
        if a[i] > x:
            cnt += 1
        else:
            sum -= cnt * (cnt + 1) / 2
            cnt = 0
    if sum < k:
        return 0
    else:
        return 1

ng, ok = 0, 1<<24
while ok-ng > 1:
    mid = (ng+ok) // 2
    if(check(mid)): ok = mid
    else : ng = mid
print(ok)

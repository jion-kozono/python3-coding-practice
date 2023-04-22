import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

# https://paiza.jp/works/mondai/reviews/show/70a53aee344b0e6e6467272a55dc3ef8

# 各人に対してパーティーに同時に参加していた人数を求めるよりも、同時に参加していなかった人数を求めたほうが簡単になります。それで、そのような人数を求めることを考えます。
# その人がパーティーに参加していた時刻と重なりがなければよいので、その人より先に帰ったか、その人より後に来たかのどちらかになります。
# つまり、i 番目の人を考えたとき、ai より小さい lj の個数と、li より大きい aj の個数の合計が、同時に参加していなかった人数になります。
# これは、最初に配列 a, l をソートして、二分探索をおこなうことで高速に求めることができます。
# 答えは、他人の人数 n - 1 から同時に参加していなかった人数を引いたものになります。

n = I()
al = [LI() for _ in range(n)]
a,l = [list(i) for i in zip(*al)]

a.sort()
l.sort()

for i in range(n):
    #before : 自分たちよりも先にパーティーから帰った人数
    before = bisect.bisect_left(l,al[i][0])
    #after : 自分たちよりも後にパーティーに来た人数
    after = n-bisect.bisect_right(a,al[i][1])
    print(n-1-(before+after))

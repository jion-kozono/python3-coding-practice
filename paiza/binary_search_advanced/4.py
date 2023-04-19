import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
A = LI()

# まず、数列を連番になっている箇所で分割してみましょう。たとえば、(1, 2, 3, 4, 1, 1, 2) であれば (1, 2, 3, 4) と (1) と (1, 2) といった具合です。
# そして、それら数列たちの長さを 1 つの数列にしてみましょう。上の例でいえば、(4, 1, 2) となります。
# こうすることで、この問題は二分探索メニューの問題「パイプを切り出そう」と同じ問題になります。
# よって、連番の長さを二分探索することで、最長の長さを求めることができます。
# 実は、数列を変換しなくても、直接二分探索で答えを求めることができます。
# 固定した長さを x とすると、手前から長さ x の連番をできるだけとっていけばよいです。
# 配列を順番に見ていき、現在見ている連番の長さを増やしながら、x 以上になったタイミングで連番の個数を 1 増やします。ただし、連番の個数を増やしたとき、つまり長さ x の連番をとったときと、a[i] + 1 == a[i + 1] が成り立たなくなったときは連番の長さをリセットすることに注意しましょう。
# こうして求めた連番の個数が K 以上かどうかを判定して、二分探索をおこなっていけばよいです。
# よって、連番の個数が K 以上であるような最大の長さを left, K より少ないような最小の長さを right として、中央の値 mid を用いて判定、更新を繰り返せばよいです。

# 長さxの連番の合計が K 以上の時は true，小さいときは false を返す．
def check(x):
    cnt = 0 # 連番の長さ
    sum = 0 # 連番の個数
    for i in range(n):
        cnt += 1
        if cnt >= x: # 連番の長さがx以上になったら連番の個数を１つ増やす
            sum += 1
            cnt = 0 # 連番の長さをリセット
        if i != n-1:
            if A[i]+1 != A[i+1]:
                cnt = 0 # a[i] + 1 == a[i + 1] が成り立たなくなったときは連番の長さをリセット
    if sum >= k  : return 1
    else : return 0

ok, ng = 0, 1<<47
while abs(ok-ng) > 1:
    mid = (ng+ok) // 2
    if(check(mid)): ok = mid
    else : ng = mid
print(ok)

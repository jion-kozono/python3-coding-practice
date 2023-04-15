import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())
# https://paiza.jp/works/mondai/reviews/show/f07adbb8e2ec6bdd908da1fd329218db
# このような問題では、条件を満たすような場合を仮定して考えてみましょう。すなわち、X,A,B (cm) のガムテープを使って N (cm) が得られると仮定してみましょう。
# このとき、X (cm) のガムテープを使う場合は「Ax + By = N - X」, 使わない場合は「Ax + By = N」という式が成り立ちます。
# この式の形を見て「拡張ユークリッドの式だ！」と思った方は良く勉強できている方だと思われます。しかし、答えを急がずに問題文を読んで拡張ユークリッドの定義を思い出してみましょう。
# 拡張ユークリッドの式 「Ax + By = N」 における x, y は整数ですが、今回の問題では x, y はガムテープの本数であるため、負の値を取ることがないので 0 以上の整数となります。
# つまり、この問題は拡張ユークリッドでは解けないということです。ひっかけ問題です。この問題で拡張ユークリッドの条件を意識していただけたらと思います。A の本数 x を全探索し、N - X - Ax または N - Ax が 0 以上の B の倍数となる x が存在するかを調べることでこの問題を解くことができます。
n, x, a, b = MI()

for i in range(n // a + 1):
    now = n - a * i
    if now % b == 0 or (now - x >= 0 and (now - x) % b == 0):
        print("Yes")
        break
else:
    print("No")

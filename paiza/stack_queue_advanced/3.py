import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

# https://paiza.jp/works/mondai/reviews/show/e7b0d349cc9b3e3117a35dc8377698dd

# to[x][i] が -1 でない時は、現在のマスを to[x][i] にすることで移動をすることができます。
# 問題は to[x][i] が -1 の時の移動で、この移動をするためにはマス x に止まる前のマスを覚えておく必要があります。
# では、i 回目の移動をする前に現在のマス M を覚えておき、移動先の to[to[M][i]][i+1] で -1 が出たら M に戻れば良いでしょうか？
# しかし、この方法では to[M][i+2] が -1 の時にどのマスに戻れば良いかがわからなくなってしまいます。
# そこで、訪れたマスを保持しておくスタック S を用意し、次のような実装を行ってみましょう。
# 「to[x][i]≠-1 である移動をおこなう場合、現在のマス x を S に入れ、マス to[x][i] に移動する。」
# 「to[x][i]=-1 である移動をおこなう場合、S の一番上のマスを取り出し、そのマスに移動する。」
# このように移動先と移動元を管理することで to[x][i] が -1 の場合も簡潔に処理することができます。


n,k = MI()
now = 0
to = [[0 for _ in range(k)] for _ in range(n)]
s = collections.deque()

for i in range(n):
    to_input = LI()
    for j in range(k):
        to[i][j] = to_input[j]
        to[i][j] -= 1

s.append(0)

for i in range(k):
    if (to[now][i] == -2):
        s.pop()
        now = s[-1]
    else:
        now = to[now][i]
        s.append(now)
    print(now +1)

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N, K = MI()
A = LI()

# 条件を満たす最小の区間の長さを格納する変数、区間内の要素の和を格納する変数、区間[left, right) の right を宣言します。
# ループを用いて、カウント変数を left とすることで
# 総和が K を超えるまで right を進める
# これまでの最小の長さと right - left を比較し、小さい方を最小の長さとして更新する
# right == left なら right を進め、そうでなければ区間内の要素の和から a_{left} を引く
# left を 1 進める
# というようにしゃくとり法をおこないます。
# right を進める条件文に関して、例えば 総和が K 以下の区間の最大の長さ を知りたい場合、現在の区間内の要素の和に a[right] を足しても K を超えない場合、 a[right] を足すということをしたいので、条件文は elements_sum + a[right] ≦ K となります。
# 今回は、総和が K より大きい区間の最小の長さ を知りたいので、a[right] に関わらず現在の区間内の要素の和が K 以下なら a[right] を足すので、条件文は elements_sum ≦ K とすることができます。
# また、総和が K になってもなお right を進めても、最小の区間の長さは得られないため、総和が K を超えるまで right を進めるのが最適な方法となります。
# しゃくとり法を用いて求めた条件を満たす区間の最大の長さを出力します。ただし、条件を満たす区間がなかった場合は -1 を出力します。


min_section_length = N+1
elements_sum = 0
right = 0
for left in range(N):
    while right < N and elements_sum <= K:
        elements_sum += A[right]
        right += 1

    if elements_sum <= K:
        break

    min_section_length = min(min_section_length, right - left)

    if right == left:
        right += 1
    else:
        elements_sum -= A[left]

if min_section_length == N + 1:
    print(-1)
else:
    print(min_section_length)

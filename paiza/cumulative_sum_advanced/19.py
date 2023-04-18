import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
A = LI()

# 条件を満たす区間の数を格納する変数、区間[left, right) の right を宣言します。
# ループを用いて、カウント変数を left とすることで
# right を進められるところまで進める
# right - left で条件を満たす区間の個数を求める
# 条件を満たす区間の個数を格納する変数に加算する
# left を 1 進める
# というようにしゃくとり法をおこないます。
# right を進める条件ですが、right と left が等しい場合は a[right] == a[left] となり、広義単調増加であるので right を進めます。
# また、a[right - 1] ≦ a[right] であるときも広義単調増加であるので right を進めます。
# しゃくとり法を用いて求めた条件を満たす区間の数を出力します。

section_count = 0
right = 0
for left in range(N):
    while right < N and (right == left or A[right - 1] <= A[right]):
        right += 1

    section_count += right - left

print(section_count)

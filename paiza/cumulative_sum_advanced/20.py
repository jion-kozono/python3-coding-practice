import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
C = LI()
# 条件を満たす最長の区間の長さを格納する変数、区間内に各色が含まれているかどうかを格納する配列、区間[left, right) の right を宣言します。
# ループを用いて、カウント変数を left とすることで
# right を進められるところまで進める
# これまでの最大の長さと right - left を比較し、大きい方を最大の長さとして更新する
# right == left なら right を進め、そうでなければ 色 c[left] のフラグを false にする
# left を 1 進める
# というようにしゃくとり法をおこないます。
# しゃくとり法を用いて求めた条件を満たす区間の最大の長さを出力します。
section_length = 0
color_flag = [False] * 55
right = 0
for left in range(N):
    while right < N and not color_flag[C[right]]:
        color_flag[C[right]] = True
        right += 1

    section_length = max(section_length, right - left)

    if right == left:
        right += 1
    else:
        color_flag[C[left]] = False

print(section_length)

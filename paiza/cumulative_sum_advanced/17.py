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

# 条件を満たす最長の区間の長さを格納する変数、区間内の要素の和を格納する変数、区間[left, right) の right を宣言します。
# ループを用いて、カウント変数を left とすることで
# right を進められるところまで進める
# これまでの最大の長さと right - left を比較し、大きい方を最大の長さとして更新する
# right == left なら right を進め、そうでなければ区間内の要素の和から a_{left} を引く
# left を 1 進める

max_section_length = 0
elements_sum = 0
right = 0
for left in range(N):
    while right < N and elements_sum + A[right] <= K:
        elements_sum += A[right]
        right += 1

    max_section_length = max(max_section_length, right - left)

    if right == left:
        right += 1
    else:
        elements_sum -= A[left]

print(max_section_length)

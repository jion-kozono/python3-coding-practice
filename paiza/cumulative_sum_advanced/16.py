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

# ループを用いて、カウント変数を left とすることで
# right を進められるところまで進める
# right - left で条件を満たす区間の個数を求める
# 条件を満たす区間の個数を格納する変数に加算する
# right == left なら right を進め、そうでなければ区間内の要素の和から a_{left} を引く
# left を 1 進める

section_count = 0
elements_sum = 0
right = 0
for left in range(N):
    while right < N and elements_sum + A[right] <= K:
        elements_sum += A[right]
        right += 1

    section_count += right - left

    if right == left:
        right += 1
    else:
        elements_sum -= A[left]

print(section_count)

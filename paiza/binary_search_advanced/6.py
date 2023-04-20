import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
AB = [LI() for _ in range(n)]

# 求めたい追加できる作業量をxとする
def is_ok(x):
    # sum : 作業時間の合計
    sum = 0
    for i in range(n):
        efficiency = AB[i][0]
        workload = AB[i][1] + x
        sum += (workload+efficiency-1)//efficiency

    return 1 if sum <= k else 0

ok, ng = 0, 1<<47
while abs(ok-ng) > 1:
    mid = (ng+ok) // 2
    if(is_ok(mid)): ok = mid
    else : ng = mid
print(ok)

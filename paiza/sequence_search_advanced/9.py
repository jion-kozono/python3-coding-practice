import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

s = S()
t = S()

ans = 0
for i in range(len(s) - len(t) + 1):
    if s[i : i + len(t)] == t:
        ans += 1

print(ans)

# 同じ文字の場合だめ
# print(s.count(t))

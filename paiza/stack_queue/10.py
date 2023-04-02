import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
s= S()

st = []

for i in range(N):
    # スタックの最後が(の場合、s[i]が)がきたら組み合わせがあるので、取り除く
    if len(st) > 0 and st[-1] == "(" and s[i] == ")":
        st.pop()
    else:
        st.append(s[i])

print("Yes" if len(st) == 0 else "No")

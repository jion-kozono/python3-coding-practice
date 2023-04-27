import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

# 再帰関数
def permutations(n, p):
    if len(p) == n:
        print(" ".join(map(str, p)))
        return
    for i in range(1, n + 1):
        if i in p:
            continue
        p.append(i)
        permutations(n, p)
        del p[-1]


n = int(input())
permutations(n, [])


# ライブラリを用いる方法(paizaでは順番で通らない)
# n = I()
# arr = list(range(1,n+1))

# ps = list(itertools.permutations(arr))
# for p in ps:
#     for i in range(n):
#         print(p[i], end=" ")
#     print()

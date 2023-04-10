import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,x,k = MI()
A = LI()

count = 0
for i in range(n-k+1):
    if A[i] != x:
        continue
    can = True
    for j in range(i, i+k):
        if A[j] != x:
            can = False
            break
    if can:
        count+=1
print(count)

# 別解
# n, x, k = map(int, input().split())
# a = [int(y) for y in input().split()]

# ans = 0
# left = 0
# while left < n:
#     right = left
#     while right < n and a[right] == x:
#         right += 1

#     ans += max(0, right - left - k + 1)
#     left = max(left + 1, right)

# print(ans)

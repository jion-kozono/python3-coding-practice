import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n,x = MI()
A = LI()

max_len = 0
temp_count=0
for i in range(n):
    if A[i] >= x:
        temp_count+=1
    else:
        temp_count=0
    max_len = max(temp_count, max_len)

print(max_len)

# 別解
# n, x = map(int, input().split())
# a = [int(y) for y in input().split()]

# ans = 0
# left = 0
# while left < n:
#     right = left
#     while right < n and a[right] >= x:
#         right += 1

#     ans = max(ans, right - left)
#     left = max(left + 1, right)

# print(ans)

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
A = LI()

count = 0
increase = [0] * (n - 1)
for i in range(n-1):
    if (A[i] < A[i + 1]):
        increase[i] = 1
    elif (A[i] > A[i + 1]):
        increase[i] = -1
    else:
        increase[i] = 0

zigzag = [0] * n

for i in range(n-2):
    if increase[i] == 0 or increase[i + 1] == 0:
        continue
    if increase[i] == increase[i + 1]:
        continue
    zigzag[i] = 1

ans = 0

ans = 0
left = 0
while left < n - 2:
    right = left
    while right < n - 2 and zigzag[right] == 1:
        right += 1

    range_num = right - left
    ans += range_num * (range_num - 1) // 2 + range_num
    left = max(left + 1, right)

print(ans)

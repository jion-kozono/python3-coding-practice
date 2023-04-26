import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

x1,y1 = MI()
x2,y2 = MI()

# √((x_1-x_2)^2 + (y_1-y_2)^2)

print(math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2))

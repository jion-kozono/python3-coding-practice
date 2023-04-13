import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

K = I()

words = []
for i in range(ord("a"), ord("z")+1):
    for j in range(ord("a"), ord("z")+1):
        for k in range(ord("a"), ord("z")+1):
            word = chr(i) + chr(j) + chr(k)
            words.append(word)

print(sorted(words)[K-1])

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

hash_table = [[] for _ in range(100)]

def hash(x, a, b): return (a * x + b) % 100

a, b = MI()
q = I()
for i in range(q):
    query, x = MI()

    h = hash(x, a, b)
    if query == 1:
        hash_table[h].append(x)
    else:
        if x in hash_table[h]:
            print("Yes")
        else:
            print("No")

for i in range(100):
    print(*hash_table[i])

import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
cards = collections.deque() #queue
graveyard = collections.deque() #stack
exclusion = collections.deque() #stack
for i in range(1, 41):
    cards.append(i)

ans = 0

for i in range(k):
    q = LS()
    query = q[0]
    if query == "game_start":
        for _ in range(5):
            x = cards.popleft()
            if x == n:
                ans = i+1
                break
    elif query == "draw":
        X = int(q[1])
        for _ in range(X):
            x = cards.popleft()
            if x == n:
                ans = i+1
                break
    elif query == "discard":
        X = int(q[1])
        for _ in range(X):
            x = cards.popleft()
            graveyard.append(x)
    elif query == "return_from_the_graveyard":
        X = int(q[1])
        for _ in range(X):
            x = graveyard.pop()
            cards.append(x)
    elif query == "exclude":
        X = int(q[1])
        for _ in range(X):
            x = cards.popleft()
            exclusion.append(x)
    else: #return_from_the_exclusion
        X = int(q[1])
        for _ in range(X):
            x = exclusion.pop()
            cards.append(x)
    if ans: break

print(ans if ans else "Lose")

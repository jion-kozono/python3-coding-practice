import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n, k = MI()
p1 = collections.deque()
p2 = collections.deque()
for i in range(n):
    hand = LS()
    p1.append(hand[0])
    p2.append(hand[1])

p1_win_cnt = 0
p2_win_cnt = 0

for i in range(k):
    q = LS()
    p1_hand = p1.popleft()
    p2_hand = p2.popleft()
    # when p1 win
    if p1_hand == "R" and p2_hand == "S" or p1_hand == "S" and p2_hand == "P" or p1_hand == "P" and p2_hand == "R":
        p1_win_cnt+=1
    # when p2 win
    if p2_hand == "R" and p1_hand == "S" or p2_hand == "S" and p1_hand == "P" or p2_hand == "P" and p1_hand == "R":
        p2_win_cnt+=1
    # when draw
    # nothing to do

    if q[0] == "push":
        p1.append(p1_hand)
    if q[1] == "push":
        p2.append(p2_hand)

if p1_win_cnt > p2_win_cnt:
    print("paiza")
elif p1_win_cnt == p2_win_cnt:
    print("draw")
else:
    print("kyoko")

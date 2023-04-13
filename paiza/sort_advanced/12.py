import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
campaign = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    l,r = MI()
    campaign[i][0] = l
    campaign[i][1] = r

campaign.sort(key=lambda x:x[1])

participated_campaigns_count = 0
campaign_last_day = 0
for i in range(n):
    if campaign_last_day < campaign[i][0]:
        participated_campaigns_count+=1
        campaign_last_day = campaign[i][1]
print(participated_campaigns_count)

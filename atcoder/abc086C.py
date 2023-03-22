N = int(input())
# 不可能な場合を列挙
# 1. 時間tが距離に対して足りない時
# 2. 距離と時間のパリティが合わない場合 ex: t=3, distance is 2 [(x,y) = (0,0) to (x,y) = (1,1)] 3 と 2はそれぞれ偶数と奇数なので到達不可能
can = True
px,py,pt = 0

for i in range(N):
    t,x,y = map(int, input().split())
    dist = abs(x - px) + abs(y - py)
    T = t - pt
    if T < dist and T % 2 != dist % 2:
        can = False
        break

print("Yes" if can else "No")

n = int(input())

# X,Y = [],[]
# for i in range(n):
#     x, y = map(int, input().split())
#     X.append(x)
#     Y.append(y)
# https://paiza.jp/works/mondai/reviews/show/3db129bb4b7b12303714e17d119bd088
points = [[int(x) for x in input().split()] for _ in range(n)]
xn, yn = points[-1]

k = int(input())

ans = 0

# for i in range(n):
for xi, yi in points:
    dist = abs(xi-xn) + abs(yi-yn)
    if dist <= k:
        ans+=1

print(ans)

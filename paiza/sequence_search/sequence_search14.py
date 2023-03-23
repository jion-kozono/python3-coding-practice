# n = int(input())
# pointsOf = {}
# for i in range(n):
#     name, point = input().split()
#     point = int(point)
#     pointsOf[name] = point

# k = int(input())

# for name, point in pointsOf.items():
#     if point >= k:
#         print(name)

# https://paiza.jp/works/mondai/reviews/show/28ad284ce9f677d9248ce5f8461463a1
# 以下の方が簡略的
n = int(input())
results = [input().split() for _ in range(n)]
k = int(input())

for name, score in results:
    if int(score) >= k:
        print(name)

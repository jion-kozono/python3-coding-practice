from collections import defaultdict

N, K, R = map(int, input().split())

location = defaultdict(int)
binary_tree = [-1] * 1000000

location[R] = 0
binary_tree[0] = R

for _ in range(N - 1):
    a, b = map(int, input().split())
    if b < a:
        location[b] = 2 * location[a] + 1
    else:
        location[b] = 2 * location[a] + 2
    binary_tree[location[b]] = b

for _ in range(K):
    now = 0
    q = int(input())

    while binary_tree[now] != -1:
        if q == binary_tree[now]:
            print("Yes")
            break
        if q < binary_tree[now]:
            now = 2 * now + 1
        else:
            now = 2 * now + 2
    if binary_tree[now] == -1:
        print("No")

# 別解
# N, K, R = map(int, input().split())

# edge = []
# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     edge.append([a, b])

# for _ in range(K):
#     q = int(input())
#     for a, b in edge:
#         if q == a or q == b:
#             print("Yes")
#             break
#     else:
#         print("No")
